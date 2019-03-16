from .models import RDFModel, InstanceModel


def get(id_: str, type_: str, api_name: str, session: scoped_session,
        path: str = None) -> Dict[str, str]:
    """Retrieve an Instance with given ID from the database [GET].
    :param id_: id of object to be fetched
    :param type_: type of object
    :param api_name: name of api specified while starting server
    :param session: sqlalchemy scoped session
    :param path: endpoint
    :return: response to the request


    Raises:
        ClassNotFound: If the `type_` is not a valid/defined RDFClass.
        InstanceNotFound: If no Instance of the 'type_` class if found.

    """
    object_template = {
        "@type": "",
    }  # type: Dict[str, Any]
    try:
        rdf_class = RDFModel.objects.filter(name=type_).first()
    except NoResultFound:
        raise ClassNotFound(type_=type_)

    try:
        instance = InstanceModel.objects.filter(pk=id_, type_=rdf_class.pk).first()
    except NoResultFound:
        raise InstanceNotFound(type_=rdf_class.name, id_=id_)

    data_IAC = session.query(triples).filter(
        triples.GraphIAC.subject == id_).all()

    data_III = session.query(triples).filter(
        triples.GraphIII.subject == id_).all()

    data_IIT = session.query(triples).filter(
        triples.GraphIIT.subject == id_).all()

    for data in data_IAC:
        prop_name = session.query(properties).filter(
            properties.id == data.predicate).one().name
        class_name = session.query(RDFModel).filter(
            RDFModel.id == data.object_).one().name
        object_template[prop_name] = class_name

    for data in data_III:
        prop_name = session.query(properties).filter(
            properties.id == data.predicate).one().name
        instance = session.query(Instance).filter(
            Instance.id == data.object_).one()
        # Get class name for instance object
        inst_class_name = session.query(RDFModel).filter(
            RDFModel.id == instance.type_).one().name
        doc = get_doc()
        nested_class_path = ""
        for collection in doc.collections:
            if doc.collections[collection]["collection"].class_.path == inst_class_name:
                nested_class_path = doc.collections[collection]["collection"].path
                object_template[prop_name] = "/{}/{}/{}".format(
                    api_name, nested_class_path, instance.id)
                break

        if nested_class_path == "":
            object_template[prop_name] = "/{}/{}/".format(
                api_name, inst_class_name)

    for data in data_IIT:
        prop_name = session.query(properties).filter(
            properties.id == data.predicate).one().name
        terminal = session.query(Terminal).filter(
            Terminal.id == data.object_).one()
        try:
            object_template[prop_name] = terminal.value
        except BaseException:
            # If terminal is none
            object_template[prop_name] = ""
    object_template["@type"] = rdf_class.name

    if path is not None:
        object_template["@id"] = "/{}/{}Collection/{}".format(
            api_name, path, id_)
    else:
        object_template["@id"] = "/{}/{}Collection/{}".format(
            api_name, type_, id_)

    return object_template

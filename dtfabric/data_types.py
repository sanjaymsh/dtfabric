# -*- coding: utf-8 -*-
"""Data type definitions."""

import abc

from dtfabric import definitions

# TODO: BooleanDefinition allow to set false_value to None in definition.
# TODO: complete EnumerationDefinition.
# TODO: complete FormatDefinition.


class DataTypeDefinition(object):
  """Data type definition interface.

  Attributes:
    aliases (list[str]): aliases.
    byte_order (str): byte-order the data type.
    description (str): description.
    name (str): name.
    urls (list[str]): URLs.
  """

  TYPE_INDICATOR = None

  _IS_COMPOSITE = False

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes a data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(DataTypeDefinition, self).__init__()
    self.aliases = aliases or []
    self.byte_order = definitions.BYTE_ORDER_NATIVE
    self.description = description
    self.name = name
    self.urls = urls

  @abc.abstractmethod
  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """

  @abc.abstractmethod
  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """

  def IsComposite(self):
    """Determines if the data type is composite.

    A composite data type consists of other data types.

    Returns:
      bool: True if the data type is composite, False otherwise.
    """
    return self._IS_COMPOSITE


class FixedSizeDataTypeDefinition(DataTypeDefinition):
  """Fixed-size data type definition.

  Attributes:
    size (int|list[int]): size of the data type.
    units (str): units of the size of the data type.
  """

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes a fixed-size data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(FixedSizeDataTypeDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.size = None
    self.units = u'bytes'

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    return [u'value']

  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """
    if self.units == u'bytes':
      return self.size


class BooleanDefinition(FixedSizeDataTypeDefinition):
  """Boolean data type definition.

  Attributes:
    false_value (int): value of False, None represents any value except that
      defined by true_value.
    true_value (int): value of True, None represents any value except that
      defined by false_value.
  """

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_BOOLEAN

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes a boolean data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(BooleanDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.false_value = 0
    self.true_value = None


class CharacterDefinition(FixedSizeDataTypeDefinition):
  """Character data type definition."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_CHARACTER


class ConstantDefinition(DataTypeDefinition):
  """Constant data type definition.

  Attributes:
    value (int): constant value.
  """

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_CONSTANT

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes an enumeration data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(ConstantDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.value = None

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    return [u'constant']

  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """
    return


class EnumerationValue(object):
  """Enumeration value.

  Attributes:
    aliases (list[str]): aliases.
    description (str): description.
    name (str): name.
    value (int): value.
  """

  def __init__(self, name, value, aliases=None, description=None):
    """Initializes an enumeration value.

    Args:
      name (str): name.
      value (int): value.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
    """
    super(EnumerationValue, self).__init__()
    self.aliases = aliases or []
    self.description = description
    self.name = name
    self.value = value


class EnumerationDefinition(FixedSizeDataTypeDefinition):
  """Enumeration data type definition.

  Attributes:
    values_per_name (dict[str, EnumerationValue]): enumeration values per name.
    values(list[EnumerationValue]): enumeration values.
  """

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_ENUMERATION

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes an enumeration data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(EnumerationDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.values = []
    self.values_per_name = {}

    # TODO: support lookup of enumeration value by alias.
    # TODO: support lookup of enumeration value by value.

  def AddValue(self, name, value, aliases=None, description=None):
    """Adds an enumeration value.

    Args:
      name (str): name.
      value (int): value.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.

    Raises:
      KeyError: if the enumeration value already exists.
    """
    if name in self.values_per_name:
      raise KeyError(u'Value: {0:s} already exists.'.format(name))

    # TODO: check if aliases already exist.
    # TODO: check if value already exists.

    enumeration_value = EnumerationValue(
        name, value, aliases=aliases, description=description)

    self.values.append(enumeration_value)
    self.values_per_name[name] = enumeration_value


class FloatingPointDefinition(FixedSizeDataTypeDefinition):
  """Floating point data type definition."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_FLOATING_POINT


class FormatDefinition(DataTypeDefinition):
  """Data format definition."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_FORMAT

  _IS_COMPOSITE = True

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    return []

  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """
    return


class IntegerDefinition(FixedSizeDataTypeDefinition):
  """Integer data type definition.

  Attributes:
    format (str): format of the data type.
  """

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_INTEGER

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes an integer data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(IntegerDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.format = definitions.FORMAT_SIGNED


class ElementSequenceDataTypeDefinition(DataTypeDefinition):
  """Element sequence data type definition.

  Attributes:
    elements_data_size (int): data size of the sequence elements.
    elements_data_size_expression (str): expression to determine the data
        size of the sequenc eelements.
    element_data_type (str): name of the sequence element data type.
    element_data_type_definition (DataTypeDefinition): sequence element
        data type definition.
    number_of_elements (int): number of sequence elements.
    number_of_elements_expression (str): expression to determine the number
        of sequence elements.
  """

  _IS_COMPOSITE = True

  def __init__(
      self, name, data_type_definition, aliases=None, data_type=None,
      description=None, urls=None):
    """Initializes a sequence data type definition.

    Args:
      name (str): name.
      data_type_definition (DataTypeDefinition): sequence element data type
          definition.
      aliases (Optional[list[str]]): aliases.
      data_type (Optional[str]): name of the sequence element data type.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(ElementSequenceDataTypeDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.byte_order = getattr(
        data_type_definition, u'byte_order', definitions.BYTE_ORDER_NATIVE)
    self.elements_data_size = None
    self.elements_data_size_expression = None
    self.element_data_type = data_type
    self.element_data_type_definition = data_type_definition
    self.number_of_elements = None
    self.number_of_elements_expression = None

  @abc.abstractmethod
  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """

  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """
    if self.element_data_type_definition:
      if self.elements_data_size:
        return self.elements_data_size

      if self.number_of_elements:
        element_byte_size = self.element_data_type_definition.GetByteSize()
        if element_byte_size:
          return element_byte_size * self.number_of_elements


class SequenceDefinition(ElementSequenceDataTypeDefinition):
  """Sequence data type definition."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_SEQUENCE

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    return [u'elements']


class StreamDefinition(ElementSequenceDataTypeDefinition):
  """Stream data type definition."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_STREAM

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    return [u'stream']


class StringDefinition(ElementSequenceDataTypeDefinition):
  """String data type definition.

  Attributes:
    encoding (str): string encoding.
    string_terminator (int): element value that indicates the end-of-string.
  """

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_STRING

  _IS_COMPOSITE = True

  def __init__(
      self, name, data_type_definition, aliases=None, data_type=None,
      description=None, urls=None):
    """Initializes a string data type definition.

    Args:
      name (str): name.
      data_type_definition (DataTypeDefinition): string element data type
          definition.
      aliases (Optional[list[str]]): aliases.
      data_type (Optional[str]): name of the string element data type.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(StringDefinition, self).__init__(
        name, data_type_definition, aliases=aliases, data_type=data_type,
        description=description, urls=urls)
    self.encoding = u'ascii'
    self.string_terminator = None

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    return [u'string']


class StructureDefinition(DataTypeDefinition):
  """Structure data type definition.

  Attributes:
    members (list[DataTypeDefinition]): members.
  """

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_STRUCTURE

  _IS_COMPOSITE = True

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes a data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(StructureDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self._attribute_names = None
    self._byte_size = None
    self.members = []

  def AddMemberDefinition(self, member_definition):
    """Adds structure member definition.

    Args:
      member_definition (DataTypeDefinition): structure member data type
          definition.
    """
    self._attribute_names = None
    self._byte_size = None
    self.members.append(member_definition)

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    if self._attribute_names is None:
      self._attribute_names = []
      for member_definition in self.members:
        self._attribute_names.append(member_definition.name)

    return self._attribute_names

  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """
    if self._byte_size is None and self.members:
      self._byte_size = 0
      for member_definition in self.members:
        byte_size = member_definition.GetByteSize()
        if byte_size is None:
          self._byte_size = None
          break

        self._byte_size += byte_size

    return self._byte_size


class StructureMemberDefinition(DataTypeDefinition):
  """Structure data type member definition.

  Attributes:
    member_data_type (str): structure member data type.
    member_data_type_definition (DataTypeDefinition): structure member
        data type definition.
  """

  def __init__(
      self, name, data_type_definition, aliases=None, data_type=None,
      description=None, urls=None):
    """Initializes a structure member definition.

    Args:
      name (str): name.
      data_type_definition (DataTypeDefinition): structure member data type
          definition.
      aliases (Optional[list[str]]): aliases.
      data_type (Optional[str]): structure member data type.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(StructureMemberDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.byte_order = getattr(
        data_type_definition, u'byte_order', definitions.BYTE_ORDER_NATIVE)
    self.member_data_type = data_type
    self.member_data_type_definition = data_type_definition

  def GetAttributeNames(self):
    """Determines the attribute (or field) names of the data type definition.

    Returns:
      list[str]: attribute names.
    """
    if self.member_data_type_definition:
      return self.member_data_type_definition.GetAttributeNames()

  def GetByteSize(self):
    """Retrieves the byte size of the data type definition.

    Returns:
      int: data type size in bytes or None if size cannot be determined.
    """
    if self.member_data_type_definition:
      return self.member_data_type_definition.GetByteSize()

  def IsComposite(self):
    """Determines if the data type is composite.

    A composite data type consists of other data types.

    Returns:
      bool: True if the data type is composite, False otherwise.
    """
    return (self.member_data_type_definition and
            self.member_data_type_definition.IsComposite())


class UUIDDefinition(FixedSizeDataTypeDefinition):
  """UUID (or GUID) data type definition."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_UUID

  _IS_COMPOSITE = True

  def __init__(self, name, aliases=None, description=None, urls=None):
    """Initializes an UUID data type definition.

    Args:
      name (str): name.
      aliases (Optional[list[str]]): aliases.
      description (Optional[str]): description.
      urls (Optional[list[str]]): URLs.
    """
    super(UUIDDefinition, self).__init__(
        name, aliases=aliases, description=description, urls=urls)
    self.size = 16

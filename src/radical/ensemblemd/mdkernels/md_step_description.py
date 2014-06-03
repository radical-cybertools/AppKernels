__copyright__ = "Copyright 2013-2014, http://radical.rutgers.edu"
__license__   = "MIT"

import saga.attributes as attributes

# ------------------------------------------------------------------------------
# Attribute description keys
KERNEL                 = 'kernel'
MIN_VERSION            = 'min_version'
ARGUMENTS              = 'arguments'
INPUT_DATA             = 'input_data'
OUTPUT_DATA            = 'output_data'

# ------------------------------------------------------------------------------
#
class MDStepDescription(attributes.Attributes) :
    """An MDStepDescription object describes a single MD step (kernel / engine
       invocation) independently from any system specifics, like paths, etc.

    .. note:: An MDStepDescription **MUST** define at least a :data:`kernel` and
              a list of :data:`attributes`.

    **Example**::

        # TODO 

    .. data:: kernel 

       (`Attribute`) The name of the MD engine / kernel to use (`string`) [`mandatory`].

    .. data:: min_version 

       (`Attribute`) The minimum MD engine / kernel version required (`string`) [`optional`].

    .. data:: arguments 

       (`Attribute`) The arguments to pass to :data:`kernel` (`list` of `strings`) [`mandatory`].

    .. data:: input_data 

       (`Attribute`) The input files that need to be transferred before execution (`transfer directive string`) [`optional`].

       .. note:: TODO: Explain transfer directives.

    .. data:: output_data 

       (`Attribute`) The output files that need to be transferred back after execution (`transfer directive string`) [`optional`].

       .. note:: TODO: Explain transfer directives.

    """
    def __init__(self):
        """Le constructeur.
        """ 

        # initialize attributes
        attributes.Attributes.__init__(self)

        # set attribute interface properties
        self._attributes_extensible  (False)
        self._attributes_camelcasing (True)

        # register properties with the attribute interface
        self._attributes_register(KERNEL,        None, attributes.STRING, attributes.SCALAR, attributes.WRITEABLE)
        self._attributes_register(ARGUMENTS,     None, attributes.STRING, attributes.VECTOR, attributes.WRITEABLE)
        self._attributes_register(MIN_VERSION,   None, attributes.STRING, attributes.VECTOR, attributes.WRITEABLE)
        self._attributes_register(INPUT_DATA,    None, attributes.STRING, attributes.VECTOR, attributes.WRITEABLE)
        self._attributes_register(OUTPUT_DATA,   None, attributes.STRING, attributes.VECTOR, attributes.WRITEABLE)

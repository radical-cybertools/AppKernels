__copyright__ = "Copyright 2014, http://radical.rutgers.edu"
__license__   = "MIT"
__author__    = "Ole Weidner <ole.weidner@rutgers.edu>"

from logger            import logger
import saga.attributes as attributes

# ------------------------------------------------------------------------------
# MDTaskDescription attribute description keys
KERNEL                 = 'kernel'
MIN_VERSION            = 'min_version'
ARGUMENTS              = 'arguments'
INPUT_DATA             = 'input_data'
OUTPUT_DATA            = 'output_data'

# ------------------------------------------------------------------------------
# Additional BoundMDTask attribute description keys
EXECUTABLE             = 'executable'
RESOURCE               = 'resource'

# ------------------------------------------------------------------------------
#
class BoundMDTask(attributes.Attributes) :
    """A BoundMDTask object is a read-only data-strucutre that defines specific 
       executables and arguments for an MD kernel / engine invocation on a 
       specific resource.

    .. data:: executable 

       (`Attribute`) The executable (`string`).

    .. data:: arguments 

       (`Attribute`) The arguments to the executable (`list of strings`).

    .. data:: resource 

       (`Attribute`) The resource this BoundMDTask was bound to (`string`).

    .. data:: input_data 

       (`Attribute`) The input files that need to be transferred before execution (`transfer directive string`).

    .. data:: output_data 

       (`Attribute`) The output files that need to be transferred back after execution (`transfer directive string`).

    """
    def __init__(self, _executable, _arguments, _resource, _input_data, _output_data):
        """Le constructeur.
        """ 

        # initialize attributes
        attributes.Attributes.__init__(self)

        # set attribute interface properties
        self._attributes_extensible  (False)
        self._attributes_camelcasing (True)

        # register properties with the attribute interface
        self._attributes_register(EXECUTABLE,    _executable,  attributes.STRING, attributes.SCALAR, attributes.READONLY)
        self._attributes_register(ARGUMENTS,     _arguments,   attributes.STRING, attributes.VECTOR, attributes.READONLY)
        self._attributes_register(RESOURCE,      _resource,    attributes.STRING, attributes.SCALAR, attributes.READONLY)
        self._attributes_register(INPUT_DATA,    _input_data,  attributes.STRING, attributes.VECTOR, attributes.READONLY)
        self._attributes_register(OUTPUT_DATA,   _output_data, attributes.STRING, attributes.VECTOR, attributes.READONLY)

# ------------------------------------------------------------------------------
#
class MDTaskDescription(attributes.Attributes) :
    """An MDTaskDescription object describes a single MD step (kernel / engine
       invocation) independently from any system specifics, like paths, etc.

    .. note:: An MDTaskDescription **MUST** define at least a :data:`kernel` and
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


    def bind(self, resource, cores):
        """Binds a class:`radical.ensemblemd.mdkernels.MDTaskDescription` to a 
           specific resource. The resulting class:`radical.ensemblemd.mdkernels.BoundMDTask`
           contains the description of executables and arguments necessary to 
           execute the MDTask on the specified resource.
        """
        bmds = BoundMDTask(
            _executable=None, 
            _arguments=[], 
            _resource=resource, 
            _input_data=[], 
            _output_data=[]
        )

        return bmds

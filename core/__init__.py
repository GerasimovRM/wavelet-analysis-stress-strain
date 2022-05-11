
try:
    import matplotlib.pyplot as plt
except ImportError:
    class PltDummy():
        def __getattr__(self, name):
            raise ValueError("`ssqueezepy.visuals` requires "
                             "`matplotlib` installed.")
    plt = PltDummy()


from . import utils
from . import ssqueezing
from . import _cwt
from . import _stft
from . import _ssq_cwt
from . import _ssq_stft
from . import _gmw
from . import _test_signals
from . import wavelets
from . import ridge_extraction
from . import toolkit
from . import visuals
from . import algos
from . import configs
from . import experimental


from .ssqueezing import *
from ._cwt import *
from ._stft import *
from ._ssq_cwt import *
from ._ssq_stft import *
from ._gmw import *
from ._test_signals import *
from .wavelets import *
from .ridge_extraction import *
from .utils.fft_utils import *

from .configs import IS_PARALLEL, USE_GPU


def wavs():
    return wavelets.Wavelet.SUPPORTED


_modules_toplevel = [
    '_cwt', '_gmw', '_ssq_cwt', '_ssq_stft', '_stft', '_test_signals', 'algos',
    'configs', 'experimental', 'ridge_extraction', 'ssqueezing', 'toolkit',
    'visuals', 'wavelets', 'utils'
]

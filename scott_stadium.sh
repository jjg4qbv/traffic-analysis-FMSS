#!/bin/bash

../../bin/prism scott_stadium{.prism,.props} -prop 1 -multirounding -multimaxciter 500 -baselineaccuracy 200 -increasefactor 1.01 -paretoepsilon 0.001 -logcpareto -gs -exportstrat scott_stadium.strat 2>&1 1> scott_stadium.log &

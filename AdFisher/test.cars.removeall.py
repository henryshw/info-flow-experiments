import adfisher

site_file = 'cars.txt'
log_file = 'log.cars.removeall.txt'

## Set up treatments

treatment1 = adfisher.Treatment("cars")
treatment1.opt_in()
treatment1.visit_sites(site_file)

treatment2 = adfisher.Treatment("cars-removeall")
treatment2.opt_in()
treatment2.visit_sites(site_file)
treatment2.remove_interest("")


## Run Experiment

adfisher.run_experiment(treatments=[treatment1, treatment2], samples=2, blocks=100, reloads=10, log_file=log_file, timeout=1000)

## Analyze Data

adfisher.run_analysis(log_file, verbose=True)

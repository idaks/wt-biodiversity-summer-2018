# wt-biodiversity-summer-2018
### Refer to the following files or folder for latest progress:
1. Magnolia_all.ipynb for species co-occurence distribution visualization function. 

- all the Mangolia distribution datasets are in the folder: /Magnolia/dataset/geocoded/

2. Refer to Magnolia folder for the Euler/x taxonomy alignment use case.  /Magnolia/EulerRuns/

3. Download the plotdata.py if you want to run the species occurrence distribution visualization individually.

4. ConceptMapping.ipynb automated the mapping process and create mock datasets.

### Ideal Workflow:

```                                           
                                        Decide which species we want to examine 
                                                       ⏬
                      Domain experts (systematists) provide a 'concept mapping' table for taxonomies over time
                                                       ⏬
                                          Euler/X taxonomy alignments 
                                                       ⏬
                            Gather species occurrence datasets (Source: SERENEC; metadata:Darwin-Core)
                                                       ⏬
                              Geocode the dataset where Lat-Long data are missing (using geocode.py)
                                                       ⏬
                                 Visualize species co-occurrence distribution 
                                                       ⏬
                                            niche modeling analysis
                                                      
```

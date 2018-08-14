# WholeTale Summer Internship 2018
## Taxonomy alignment as a key to enhance reproducibility in biodiversity research: a case study of Magnolia 

Author: Yi-Yun Cheng (Jessica), University of Illinois at Urbana-Champaign

Mentors: Dr. Bertram Ludaescher, UIUC ; Dr. Nico Franz, ASU

### Goal of this project
Oftentimes in biodiversity research, we expect the scientific names of species to be unique identifiers, but actually they may not be. Why is that?

(1) The scientific names can vary over time

(2) The names stay the same, but the semantics of the names change

Other complicated issues:

(1) Different people may have different perceptions to the taxonomy of a same topic

(2) Species distribution datasets oftentimes only include information on a species ‘name’ without crediting the authorship of that taxonomy

This is why we are in a pressing need to align diffferent taxonomies that is addressing the same topic, not to only make the names more interoperable, but also to make way for further datasets usage.

### Overview of the tasks for this project
**Step 1**: Decide which species (or genus) to examine

**Step 2**: Domain experts provide a mapping table for the taxonomies used over time for that particular species

**Step 3**: Researcher transpose domain experts’ table into Euler/X or LeanEuler input file

**Step 4**: Gather species distribution dataset from biodiverisity portals

**Step 5**: Concept mapping of the taxonomies and create new datasets based on different taxonomies

**Step 6**: Data cleaning - geocode missing lat-long information

**Step 7**: Visualizing species co-occurrence distribution & synthesized taxonomy alignment distribution

**Step 8**: Niche modeling and further analyisis

### Refer to the following for details
1. **Step 5**: Concept mapping process. Refer to [this notebook](https://github.com/idaks/wt-biodiversity-summer-2018/blob/master/ConceptMapping/ConceptMapping-MagnoliaMapping_correct.ipynb)

2. **Step 6**: Filling in missing geo-location information. Clone [this repository](https://github.com/idaks/intros-MaxEnt/tree/master/introsmaxent) and run the [geocode.py](https://github.com/intros-MaxEnt/introsmaxent/geocode.py) along with [testgeocode.py](https://github.com/idaks/intros-MaxEnt/blob/master/introsmaxent/test_geocode.py).

3. **Step 7**: Species co-occurrence distribution visualization. Refer to [this notebook](https://github.com/idaks/wt-biodiversity-summer-2018/blob/master/Magnolia_all.ipynb)
  - try [plotdata.py](https://github.com/idaks/wt-biodiversity-summer-2018/blob/master/plotdata.py) to run the code directly

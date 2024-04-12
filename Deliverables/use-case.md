# Narrative

The United States Department of Agriculture(USDA), local farmers, and the United Nations have expressed an interest in maximizing efficient land use for future farm and renewable energy developments. However, finding suitable land for these projects can be arduous and depends on many factors, such as soil quality, terrain, pollution, and other factors that influence crop growth or energy efficiency. This project is intended to provide a tool to query the relevant aggregated data to support the exploration and identification of quality land for agriculture and renewable energy use. The primary users of this tool would be local farmers, government entities, and scientific researchers.

Unfortunately, the data that should be used for determining the ideal location for these future land use projects are dispersed among many different entities, require specialized tools to navigate through, or may be difficult to understand without a background in a specific field of study. By implementing a knowledge graph, the appropriate relationships between the available data can be easily identified and used to generate a dataset, which will aid users in identifying the most appropriate locations for their future land development projects. Optimizing this process for users will generate many benefits, including enhanced food security, economic growth, and increased access to reusable energy, which are goals that align with both local and global communities in creating a more sustainable future.

The focus of KG-LandUse will be on the relevant data for the state of Ohio, as it is where the university funding this research resides. However, the schema for this knowledge graph can likely be reused to determine the best land use for any geographic location.

# Competency Questions

1. What are the geographic coordinates for the top 10 most highly rated soil quality locations for croplands within Ohio?
2. Which crops are best suited for [soil type]?
3. Does [geographic location] have a low or high risk of flooding?
4. What location within 35 miles of Columbus, Ohio, has the most water access and is suitable for farming?

# Potential Datasets & Existing Ontologies

### Toolsets

- [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/index-geonet-allcontent.html)
- [USDA Web Soil Survey Interactive Map](https://websoilsurvey.nrcs.usda.gov/app/WebSoilSurvey.aspx)

### Datasets

- [gNATSGO and gSSURGO Soil Survey Data](https://nrcs.app.box.com/v/soils/folder/17971946225)

### Ontologies

- [Ontology: Land Use](https://enterpriseintegrationlab.github.io/icity/LandUse/LandUse_1.2/doc/index-en.html#CLUMPClassification)

### NameSpaces

- [Namespace: Open Street Map Land Use](https://wiki.openstreetmap.org/wiki/Map_features#Landuse)

# Useful Links

### Agriculture

- [Food and Agriculture Organization of the United Nations: Sustainable Land Management](https://www.fao.org/land-water/land/sustainable-land-management/en/)
- [USDA Crop Production](https://www.usda.gov/topics/farming/crop-production)
- [USDA: Land Evaluation](https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/land/evaluation-and-assessment)
- [USDA: National Cooperative Soil Survey](https://www.nrcs.usda.gov/about/partner-with-us/national-cooperative-soil-survey)

### General Info

- [Midwest Renewable Energy Land Use Challenges](https://www.nature.org/en-us/about-us/where-we-work/united-states/midwest-demand-for-renewables/)
- [Solar Energy Industries Association: Project Developments](https://www.seia.org/research-resources/major-solar-projects-list)

### Research

- [An Ontology-Based Framework for Geospatial Integration and Querying of Raster Data Cube Using VKG](https://pdfs.semanticscholar.org/1ddc/75800e154748192bb07f92843ea17d6f0475.pdf)
- [Semantic Querying of Integrated Raster and Relational Data](https://ceur-ws.org/Vol-3485/paper8240.pdf)

### Spatial Imagery

- [Spatial Data Science](https://r-spatial.org/book/part-1.html)
- [Advanced Rapid Imaging and Analysis (ARIA)](https://aria.jpl.nasa.gov/)
- [Geographic Information Systems: Earth Data](https://www.earthdata.nasa.gov/learn/pathfinders/gis-pathfinder/find-data#gis-tools)
- [JPL Opera](https://www.jpl.nasa.gov/go/opera/about-opera)
- [Socioeconomic Data and Applications Center (SEDAC)](https://sedac.ciesin.columbia.edu/)

# Guides

- [gSSURGO ArcMAP (ArcGIS) User Guide](/UserGuides/gSSURGO_UserGuide_July2020.pdf)

  **NOTE:** Guide was created for ArcMAP, so some instructions will require identifying and using the ArcGIS counterpart to achieve results.

# Contributors

- Michael McCain

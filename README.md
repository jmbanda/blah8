# BLAH8 proposal - Towards automated phenotyping definition extraction using large language models

In this work, we propose creating a methodology and evaluation set for extracting electronic phenotype definitions in an automated fashion using large language models (GPT-4 in this case). While there have been many approaches to automatically extract phenotype definition codes and rules using NLP systems, the potential of LLMs in this context has not been deeply studied. We have shown feasibility in our recent work at the [OHDSI 2023 symposium](https://www.ohdsi.org/2023showcase-102/), but no fully automated efforts have been made. Our project will curate 10 phenotype definitions, five extracted from the [OHDSI Phenotype library](https://ohdsi.github.io/PhenotypeLibrary/) and five extracted from the [eMERGE via PheKB](https://phekb.org/). We will curate these definitions in two aspects: code sets, and logical rules. This will allow us to evaluate the LLM extracted definitions in two different levels, as code set extraction is considerably easier than logical rule extraction. The methodological component of this proposal includes the creation of prompting strategies to extract phenotype definitions from the LLM training data, as well as provided documents for extraction (biomedical literature). We will assess if only leveraging the LLM training data is sufficient to generate these phenotype definitions or if providing some additional context (biomedical literature) would improve performance. 

BLAH 8 results:

[Project updates and wrap-up](https://docs.google.com/presentation/d/1zfoxt6Kif8lygkLqJPGHxMpKzW7S04ULEcM9pWpcXpw/edit#slide=id.g2b0b983024e_1_65)

[Publication pre-print](https://www.researchsquare.com/article/rs-4798033/v1)

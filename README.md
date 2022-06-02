## Goal
The goal of this deep learning project is multi-part:
- To get experience in outsourcing and collecting data for data related projects from the web.
- To explore natural language processing as a machine learning technique as we did not cover this in class
- To set up the foundation in learning more about agriculture in Kenya, common topics and conditions for a set of crops in support of my capstone.
- To make use of pretrained models in addition to building new models for language processing.

## Main Sections (highlights)
1. Web scraping data from agricultural websites:
  1. Beautifulsoup to with 'xml' and 'html' file formats
  2. Created dataframe to store text
2. Topic modeling to get the main topics in the websites
  1. TFIDF: top n words and sentences, visualizing with word cloud
  ![][wordcloud.png]
  2. LDA: ranking topics by score
3. Summarization: abstractive and extractive using both shallow and deep learning models
  1. BERT
  2. GPT3
  3. XLNET models
  4. Rouge score
  5. Extractive summarization with sentence ranking

## Sample Text and Summary with Deep Learning
### Text

The Kenya Meteorological Department has predicted that the current dry and hot conditions in the country will continue to prevail. As a result, the long rains growing season that usually starts in March and ends in May will be delayed.  Whether this is just a cyclical pattern or the result of climate change is a subject for a separate debate. The delayed onset of rains  is already causing anxiety among farmers as they ponder on the implications of this on their yields. Maize is undoubtedly the primary staple food in Kenya. Any factor that influences maize yields is therefore of key concern to farmers. Extraneous factors such as weather patterns notwithstanding, it is important for maize farmers to pay attention to all the good standard practices needed for optimum production.
Firstly, the farmer needs to understand their agro ecological zone.  This helps determine the climatic conditions ideal for maize production and informs  correct hybrid seed choice. At this juncture, the farmer needs to understand the soil characteristics prevalent in their field. Maize is a nutrient intensive and requires adequate supplies of all nutrients for all growth stages. Fertile, well drained, well aerated and good textured soil is able to supply these nutrients.  However, soil pH determines the availability of nutrients in the soil. pH is the level of acidity or alkalinity of the soil.  Maize crops grow best at a soil pH of between 5.5 and 7.3, with pH 6.0–6.5 being optimal. In this range, nitrogen, potassium, phosphorus, calcium and magnesium are readily  available.  Nitrogen helps in establishment of healthy leaves, phosphorus for root formation, potassium for fruiting while secondary nutrients such as calcium and magnesium among others are critical for crop physiological functions. Soil testing helps establish the available nutrients and the remedial steps that need to be undertaken in case of deficiencies. Fertile soil should be well prepared for sowing. The correct tillage method ensures ample availability of all plant nutrients, water retention and reduced incidences of pests and diseases.

It is important for the farmer to prepare for sowing by selecting the correct seed.  Indeed, good seed doesn’t cost, it pays. In the case of maize, “good seed” often equates to good hybrid seed. Commercially acquired certified seeds are as a standard practice dressed with a fungicide and an insecticide to prevent diseases and insects respectively. A novel and growing practice is the further dressing with beneficial microorganisms such as Panoramix to ensure robust growth characterised by well-established root system. This improves nutrient and water use efficiency, resulting in a healthy resilient crop able to achieve higher yields. In addition, the correct sowing depth will ensure uniform emergence and good plant population. 
During, sowing it is crucial to use the right nutrient sources which include organic manure and fertilizers. Organic manure should be applied few weeks before sowing. For better fertilizer efficiency, it is important to use the 4R principles, which are the four ‘rights’ of fertilizer management  i.e. apply the right source of nutrient at the right rate, at the right time and in the right place. Maize also requires ‘booster nitrogen’ over the growing period. It is important to top dress after 25-30 days of sowing and do the final top dressing after 20-25 days of first top dressing. 
It should be noted that the emergence, comes with other unwanted plants that compete with maize for nutrients. It is important to remove the unwanted plants by weeding regularly.  If all these steps are followed, and the weather patterns are favourable, then the farmer is guaranteed of a bumper harvest. We take this opportunity to wish all maize farmers a highly productive season. 
 
### Summary
"['The Kenya Meteorological Department has predicted that the current dry and hot conditions in the country will continue to prevail.', ' This helps determine the climatic conditions ideal for maize production and informs correct hybrid seed choice.', ' At this juncture, the farmer needs to understand the soil characteristics prevalent in their field.', ' Maize is a nutrient intensive and requires adequate supplies of all nutrients for all growth stages.', ' Soil testing helps establish the available nutrients and the remedial steps that need to be undertaken in case of deficiencies.', ' Commercially acquired certified seeds are as a standard practice dressed with a fungicide and an insecticide to prevent diseases and insects respectively.', ' This improves nutrient and water use efficiency, resulting in a healthy resilient crop able to achieve higher yields.', '"

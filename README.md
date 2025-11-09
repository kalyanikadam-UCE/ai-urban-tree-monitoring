# 🌳 AI-Powered Urban Tree Monitoring

**Team Name:** Dynomic  
**Hackathon:** OneEarth International Hackathon 2025  

**Team Members:**  
- Kalyani Rajesh Kadam  
- Tanishka Balasaheb Pangavhane  

## Project Overview
Trees in cities are important because they help reduce heat, improve air quality, and support a healthy environment.  
But many times, trees become weak or infected without being noticed early.

In this project, we created a simple system that:
- Allows people to upload a picture of a tree.
- The system checks the picture and suggests whether the tree looks **healthy**, **stressed**, or **possibly diseased**.
- We also use **NDVI (a satellite vegetation index)** to check how green and healthy different areas of the city are.

This can help city authorities or communities take better care of trees before major damage happens.

## Key Features
| Feature | Description |
|--------|-------------|
| Tree Image Check | Upload a tree photo and receive a basic health condition output |
| Satellite Greenness View (NDVI) | Shows how healthy the vegetation is in different city areas |
| Dashboard View | Simple Streamlit interface for viewing results and maps |
| Community Use | Anyone can help report tree conditions |

## Tech Used
| Part | Tool |
|------|------|
| Interface | Streamlit |
| Image Classification (future integration) | PyTorch / YOLO |
| Satellite Data | Sentinel-2 NDVI |
| Optional Storage | Firebase |
| Mapping | Folium / Leafmap |

## How to Run
```bash
git clone https://github.com/kalyanikadam-UCE/ai-urban-tree-monitoring.git
cd ai-urban-tree-monitoring
pip install -r requirements.txt
streamlit run app/streamlit_app.py

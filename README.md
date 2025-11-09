# AI-Powered Urban Tree Monitoring

**Team Name:** Dynomic  
**Hackathon:** OneEarth International Hackathon 2025  

**Team Members:**  
- Kalyani Rajesh Kadam  
- Tanishka Balasaheb Pangavhane  

---

## Overview
Urban trees contribute significantly to environmental quality, heat reduction, and public well-being.  
However, detecting early signs of disease, stress, or poor vegetation health can be difficult without a systematic monitoring approach.

This project presents a tree health monitoring system that:
- Accepts tree images uploaded by users and provides a basic health assessment.
- Utilizes NDVI (Normalized Difference Vegetation Index) derived from satellite data to evaluate vegetation and canopy health across city areas.
- Displays results on an interactive dashboard for easy interpretation.

The system is designed as a low-cost, scalable tool to support community participation and informed urban green space management.

---

## Objectives
1. Enable basic tree health assessment using uploaded tree images.
2. Integrate satellite-based NDVI data for city-level vegetation monitoring.
3. Provide an accessible dashboard interface to support decision-making for tree care and urban planning.

---

## Key Features
| Feature | Description |
|--------|-------------|
| Tree Image Health Check | Allows users to upload a tree image and receive a preliminary health classification. |
| NDVI Analysis | Uses Sentinel-2 satellite vegetation index to assess the greenness of specific regions. |
| Dashboard Interface | Built using Streamlit to display image results and area-based vegetation indicators. |
| Community Reporting | Encourages public participation in urban tree monitoring. |

---

## Technology Stack
| Component | Technology |
|----------|------------|
| Interface | Streamlit |
| Image Classification (future model integration) | PyTorch / YOLO |
| Satellite Data | Sentinel-2 NDVI |
| Optional Data Storage | Firebase |
| Mapping and Visualization | Folium / Leafmap |

---

## How to Run the Application
```bash
git clone https://github.com/kalyanikadam-UCE/ai-urban-tree-monitoring.git
cd ai-urban-tree-monitoring
pip install -r requirements.txt
streamlit run app/streamlit_app.py

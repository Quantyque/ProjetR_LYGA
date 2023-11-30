import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import L from "leaflet";
import "leaflet/dist/leaflet.css";

interface LocationMarkerProps {
    onMapClick: (lat: number, lng: number) => void;
}
  
function LocationMarker({ onMapClick }: LocationMarkerProps) {
    const [position, setPosition] = useState(null);

    const markerIcon = new L.Icon({
        iconSize: [25, 41],
        iconAnchor: [10, 41],
        popupAnchor: [2, -40],
        iconUrl: "https://unpkg.com/leaflet@1.6/dist/images/marker-icon.png",
        shadowUrl: "https://unpkg.com/leaflet@1.6/dist/images/marker-shadow.png"
    });

    const map = useMapEvents({
        click(e) {
        const { lat, lng } = e.latlng;
        setPosition(e.latlng);
        onMapClick(lat, lng);
        console.log(lat, lng)
        },
        locationfound(e) {
        setPosition(e.latlng);
        map.flyTo(e.latlng, map.getZoom());
        },
    });

    return position === null ? null : (
        <Marker position={position} icon={markerIcon}>
        <Popup>You clicked here</Popup>
        </Marker>
    );
}

interface MapElementProps {
    onMapClick: (lat: number, lng: number) => void;
}

const MapElement = ({ onMapClick }: MapElementProps) => {

  return (

    <MapContainer style={{ height: "80vh", width: "100%" }} zoom={2} center={[50, 50]}>
        <TileLayer attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <LocationMarker onMapClick={(lat: number, lng: number) => onMapClick(lat, lng)} />
    </MapContainer>

  )
  
}

export default MapElement
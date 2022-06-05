import React from 'react';
import './Map.css';

class Map extends React.Component {
	state = { parks: [] };

	async componentDidMount () {
		// Asynchronously fetch the parks' geo coordinates from the API
		const response = await fetch('/api/parks');
		const parks = await response.json();

		// Once the state is set, the park markers will be added to the map
		this.setState({ parks });
	}

	render () {
		// Our map is an SVG, with height:width about 1:0.734
		// The map image has a margin around colorado, about 0.0344 the width
		const IMAGE_WIDTH = 800;
		const IMAGE_HEIGHT = IMAGE_WIDTH * 0.734;
		const IMAGE_MARGIN = IMAGE_WIDTH * 0.0344;
		const MARKER_DIAMETER = 10;
		document.body.style.setProperty('--map-width', `${IMAGE_WIDTH}px`);
		document.body.style.setProperty('--map-height', `${IMAGE_HEIGHT}px`);
		document.body.style.setProperty('--marker-diameter', `${MARKER_DIAMETER}px`);

		// Colorado's official legal boundary is complicated,
		// but for our purposes it goes from 36 N to 40 N, and from 102.0467 W to 109.0467 W
		const SOUTH = 37;
		const NORTH = 41;
		const NS_SCALE = (IMAGE_HEIGHT - 2 * IMAGE_MARGIN) / (NORTH - SOUTH);
		const EAST = 102.0467;
		const WEST = 109.0467;
		const EW_SCALE = (IMAGE_WIDTH - 2 * IMAGE_MARGIN) / (WEST - EAST);

		// We're definitely not going to do any kind of spherical projection.
		// For our purposes, the world is flat and Colorado is a rectangle.
		const createMarker = function ({ ParkId, ParkName, Latitude, Longitude }) {
			let bottom = NS_SCALE * (Latitude - SOUTH) + IMAGE_MARGIN + MARKER_DIAMETER / 2 + `px`;
			let right = EW_SCALE * (Longitude - EAST) + IMAGE_MARGIN + MARKER_DIAMETER / 2 + `px`;

			return {
				id: ParkId,
				name: ParkName,
				style: {
					bottom,
					right,
				}
			}
		}

		return (
			<div id="map">
				{this.state.parks.map(createMarker).map(marker => (
					<div
						key={marker.id}
						className="marker"
						title={marker.name}
						style={marker.style}
					></div>
				))}
			</div>
		);
	}
}

export default Map;
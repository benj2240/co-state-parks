import React from 'react';
import './Map.css';

class Map extends React.Component {
	state = { parks: [], selectedPark: null };

	async componentDidMount () {
		// Following the pattern used by https://www.valentinog.com/blog/await-react/

		// Asynchronously fetch the parks' geo coordinates from the API
		const response = await fetch('/api/parks');
		const parks = await response.json();

		// Once the state is set, the park markers will be added to the map
		this.setState({ parks, selectedPark: null });
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

		// Colorado's official legal boundary is very complicated,
		// but for our purposes it goes from 36 N to 40 N, and from 102.0467 W to 109.0467 W
		const SOUTH = 37;
		const NORTH = 41;
		const NS_SCALE = (IMAGE_HEIGHT - 2 * IMAGE_MARGIN) / (NORTH - SOUTH);
		const EAST = 102.0467;
		const WEST = 109.0467;
		const EW_SCALE = (IMAGE_WIDTH - 2 * IMAGE_MARGIN) / (WEST - EAST);

		// We're definitely not going to do any kind of spherical projection.
		// For our purposes, the world is flat and Colorado is a rectangle.
		// Markers are placed with position:absolute, offset from the southeast
		// corner of the map. This choice was largely arbitrary.
		const computeStyle = function ({ Latitude, Longitude }) {
			let bottom = NS_SCALE * (Latitude - SOUTH) + IMAGE_MARGIN + MARKER_DIAMETER / 2 + `px`;
			let right = EW_SCALE * (Longitude - EAST) + IMAGE_MARGIN + MARKER_DIAMETER / 2 + `px`;

			return { bottom, right };
		}

		// I think the proper way to do this would be to store the selected park
		// in the app root (or Redux), and let the info card be a separate component.
		let parkInfoCard;
		if (this.state.selectedPark) {
			let { ParkName, Latitude, Longitude, WikiLink } = this.state.selectedPark;
			parkInfoCard = (
				<div>
					<h2>{ParkName}</h2>
					<p>This park is at {Latitude}°N, {Longitude}°W.</p>
					<a href={WikiLink}>Learn more here!</a>
				</div>
			);
		}
		else {
			parkInfoCard = (<div>Click a park on the map above to learn more!</div>);
		}

		return (
			<div id="map">
				<div id="marker-container">
					{this.state.parks.map(park => {
						let styleObject = computeStyle(park);

						/* I am QUITE certain there is a more idiomatic way to do this */
						let selectPark = () => {
							this.setState({ parks: this.state.parks, selectedPark: park })
						};

						return (
							<button
								key={park.ParkId}
								className="marker"
								title={park.ParkName}
								style={styleObject}
								onClick={selectPark}
							></button>
						)
					})}
				</div>
				<div id="selected-park">
					{parkInfoCard}
				</div>
			</div>
		);
	}
}

export default Map;
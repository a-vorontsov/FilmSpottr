import React, {Component} from 'react';
import GoogleMapReact from 'google-map-react';
import geolib from 'geolib';
import marker from '../img/marker.svg';
import locationData from '../ukFilmLocations.json';


export default class MapDisplay extends Component {
	constructor(props) {
    super(props);
    this.state = {
    	center: [],
	    zoom: 0,
	    greatPlaceCoords: {},
	    lat: 0,
	    lng: 0,
    }
  }

  static defaultProps = {
    center: [50.0, 0.0],
    zoom: 12,
  }

	componentDidMount() {
		navigator.geolocation.getCurrentPosition(
			position => {
				this.setState({
					center: [position.coords.latitude, position.coords.longitude],
					lat: position.coords.latitude,
					lng: position.coords.longitude,
				});
			}
		);
	}

  render() {
  	navigator.geolocation.getCurrentPosition(
			(position) => {
				this.setState({
					center: [position.coords.latitude, position.coords.longitude],
					lat: position.coords.latitude,
					lng: position.coords.longitude,
				});
			}
		);

		const Marker = ({ id, title, description}) =>
			<div className="parent">
				<div className="child">
					<div className="markerWrapper">
						<img className="marker" src={marker} alt="marker"/>
					</div>
					<div className="textChild">
						<div className="shown">
							<div className="markerText">
								<a href={"https://www.imdb.com/title/" + id}>{title}</a>
							</div>
							<div className="markerText">{description}</div>
						</div>
					</div>
				</div>
			</div>;
		
		var locationArray = [];
		for (var i = 0; i < locationData.length; i++) {
			var data = locationData[i];
			const distance = geolib.getDistance({latitude: this.state.lat, longitude: this.state.lng}, {latitude: data.sceneLat, longitude: data.sceneLon});
			if (distance < 50000) {
				locationArray.push(data);
			}
		}

		const locationList = locationArray.map((marker, key) =>
			<Marker
				displayDesc={this.state.displayDesc}
				id={marker.imdbID}
				title={marker.movieTitle}
				description={marker.sceneDescription}
				key={key}
	  		lat={marker.sceneLat}
	  		lng={marker.sceneLon}/>
		);


    return (
    	<div className="mapContainer">
	      <GoogleMapReact
	      	bootstrapURLKeys={{key: 'AIzaSyC_ZiYZLIO1d0o96Z_H3cQx1LerKnwFw1c'}}
	      	defaultCenter={this.props.center}
	      	center={this.state.center}
	      	defaultZoom={14}
	      	zoom={14}
	      	>
	      	{
	      		locationList
	      	}
	      </GoogleMapReact>
      </div>
    )
  }
}
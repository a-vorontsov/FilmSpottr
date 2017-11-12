import React, {Component} from 'react';
import GoogleMapReact from 'google-map-react';
import marker from '../img/marker.svg'

const Marker = () => <div><img className="marker" src={marker} alt="marker"/></div>;

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
  };

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
			position => {
				this.setState({
					center: [position.coords.latitude, position.coords.longitude],
					lat: position.coords.latitude,
					lng: position.coords.longitude,
				});
			}
		);
    return (
    	<div className="mapContainer">
	      <GoogleMapReact
	      	bootstrapURLKeys={{key: 'AIzaSyC_ZiYZLIO1d0o96Z_H3cQx1LerKnwFw1c'}}
	      	defaultCenter={this.props.center}
	      	center={this.state.center}
	      	defaultZoom={15}
	      	zoom={15}
	      	>
	      	<Marker
	      		lat={this.state.lat}
	      		lng={this.state.lng}/>
	      	<Marker
	      		lat={50.865761}
	      		lng={-0.087263}/>
	      </GoogleMapReact>
      </div>
    )
  }
}
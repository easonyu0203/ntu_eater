import React, {useState, useEffect} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Restaurants_gallery from './Restaurants_gallery'
import MyNavbar from './MyNavbar'

export default function App(){
	

	return (
	<React.Fragment>
		<MyNavbar/>
		<Restaurants_gallery />
	</React.Fragment>
	)
}
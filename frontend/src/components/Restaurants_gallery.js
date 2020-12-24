import React, {useState, useEffect} from 'react'
import axios from 'axios'
import '../css/restarauntGallery.css'


export default function Restaurants_gallery(){
	const [data, setData] = useState([])

	useEffect(() => {
		axios.get('api/restaurant').then((res) => {
			console.log(res)
			if(res.status !== 200){
				console.log(`someting wrong when getting data from url ${res.url}`)
			}
			else{
				setData(()=>res.data)
			}
		})
	}, [])

	return (
		<React.Fragment>
			<h1>restaurant gallery</h1>
			<ul>
				{data.map(restaurant => (
					<li key={restaurant.id}>
						<ul>
							<li key='name'>name: {restaurant.name}</li>
							<li key='location'>location: {restaurant.location}</li>
							<li key='phone number'>phone number: {restaurant.phone_number}</li>
						</ul><br></br>
					</li>
				))}
			</ul>
		</React.Fragment>
	)
}
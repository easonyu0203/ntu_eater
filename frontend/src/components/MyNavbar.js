import React from 'react';
import {Navbar, Nav, Form, FormControl, Button} from 'react-bootstrap'

export default function MyNavbar(){
	return(
<>
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="/">NTU eater</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="/">Home</Nav.Link>
      <Nav.Link href="#features">Features</Nav.Link>
      <Nav.Link href="#pricing">Log In</Nav.Link>
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-info">Search</Button>
    </Form>
  </Navbar>
</>
	)
}
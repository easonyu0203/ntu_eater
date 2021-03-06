const path = require('path')
module.exports = {
	entry: './src/index.js',
	output: {
		filename: 'main.js',
		path: path.join(__dirname, 'static/frontend')
	},
	module: {
	  rules: [
		{
		  test: /\.js$/,
		  exclude: /node_modules/,
		  use: {
			loader: "babel-loader"
		  }
		},
		{
			test: /\.css$/,
			use: [
			  'style-loader',
			  'css-loader'
			]
		  }
	  ]
	},
  };
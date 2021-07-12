
const autoprefixer = require('autoprefixer')
module.exports = {
    entry: './frontend/src/index.js',
    resolve: {
        extensions: ['.js', '.jsx']
    },
    output: {
        path: __dirname + 'static/frontend',
        filename: 'main.js',
        publicPath: 'frontend/templates/frontend'
    },
    devServer: {
        contentBase: './frontend',
    },
    module:{
        rules: [
            {
                test:/\.js$/,
                exclude: /node_modules/ ,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: [
                    { loader: 'style-loader'},
                    { 
                        loader: 'css-loader',
                        options: {
                            importLoaders: 1,
                            modules: true,
                            localIdentName: '[name]__[local]__[hash:base64:5]'
                        }
                    },
                    {
                        loader: 'postcss-loader',
                        options: {
                            ident: 'postcss',
                            plugins: () => [
                                autoprefixer({
                                    browsers: [
                                        "> 1%",
                                        "last 2 versions"
                                    ]
                                })
                            ]
                        }
                    }
                ]
            }
        ]
    }
}
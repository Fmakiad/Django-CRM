/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './web/templates/web/*.html',
    './node_modules/flowbite/**/*.js'
  ],
}

//Flowbite 
module.exports = {

  plugins: [
      require('flowbite/plugin')
  ]

}
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}", // First item in the content array
    "./node_modules/flowbite/**/*.js" // Second item in the content array
  ],
  theme: {
    extend: {},
  },
  plugins: [ require('flowbite/plugin') ],
};

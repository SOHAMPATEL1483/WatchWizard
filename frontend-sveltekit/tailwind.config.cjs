const colors = require("tailwindcss/colors");

const config = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}",
  ],

  theme: {
    extend: {
      colors: {
        primary: colors.violet,
      },
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
        Lexend: ["Lexend Deca", "sans-serif"],
      },
    },
  },

  plugins: [require("flowbite/plugin")],
  darkMode: "class",
};

module.exports = config;

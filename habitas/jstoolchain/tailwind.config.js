/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../**/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwind-scrollbar'),
  ],
  safelist: [
    'bg-red-600',
    'hover:bg-red-700',
    'bg-emerald-600',
    'hover:bg-emerald-700',
  ],
  theme: { extend: {} },
}

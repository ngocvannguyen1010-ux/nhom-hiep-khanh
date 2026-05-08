import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        cream: "#FAF6F0",
        ink: "#1F1B16",
        brand: {
          50: "#FBF1E5",
          100: "#F5DDBE",
          200: "#EBB987",
          300: "#DD9251",
          400: "#C57530",
          500: "#A35E22",
          600: "#854B1B",
          700: "#6B3C16",
          800: "#522D11",
          900: "#3A1F0C",
        },
      },
      fontFamily: {
        sans: ["system-ui", "Segoe UI", "Roboto", "Helvetica", "Arial", "sans-serif"],
        serif: ["Georgia", "Cambria", "Times New Roman", "serif"],
      },
    },
  },
  plugins: [],
};

export default config;

import customtkinter as ctk
import requests
from PIL import Image, ImageTk
import io

# --- Configuration ---
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("SkyCast Weather")
        self.geometry("400x550")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Title
        self.title_label = ctk.CTkLabel(self, text="SkyCast", font=("Helvetica", 30, "bold"))
        self.title_label.pack(pady=(30, 10))

        # Search Frame
        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.search_frame.pack(pady=10, padx=20, fill="x")

        self.city_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Enter city name...", height=40)
        self.city_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.search_btn = ctk.CTkButton(self.search_frame, text="Search", width=80, height=40, command=self.get_weather)
        self.search_btn.pack(side="right")

        # Result Area (Initially Hidden)
        self.result_frame = ctk.CTkFrame(self, corner_radius=15)
        self.result_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.city_name_label = ctk.CTkLabel(self.result_frame, text="", font=("Helvetica", 22, "bold"))
        self.city_name_label.pack(pady=(20, 0))

        self.icon_label = ctk.CTkLabel(self.result_frame, text="")
        self.icon_label.pack(pady=10)

        self.temp_label = ctk.CTkLabel(self.result_frame, text="", font=("Helvetica", 50, "bold"))
        self.temp_label.pack()

        self.desc_label = ctk.CTkLabel(self.result_frame, text="", font=("Helvetica", 16, "italic"), text_color="gray")
        self.desc_label.pack()

        # Stats Grid (Humidity/Wind)
        self.stats_frame = ctk.CTkFrame(self.result_frame, fg_color="transparent")
        self.stats_frame.pack(pady=20, fill="x")

        self.hum_label = ctk.CTkLabel(self.stats_frame, text="", font=("Helvetica", 12))
        self.hum_label.pack(side="left", expand=True)

        self.wind_label = ctk.CTkLabel(self.stats_frame, text="", font=("Helvetica", 12))
        self.wind_label.pack(side="right", expand=True)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            return

        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(complete_url).json()

            if response["cod"] != "404":
                main = response["main"]
                weather = response["weather"][0]
                wind = response["wind"]

                # Update Labels
                self.city_name_label.configure(text=f"{response['name']}, {response['sys']['country']}")
                self.temp_label.configure(text=f"{round(main['temp'])}°C")
                self.desc_label.configure(text=weather['description'].capitalize())
                self.hum_label.configure(text=f"💧 Humidity: {main['humidity']}%")
                self.wind_label.configure(text=f"💨 Wind: {wind['speed']} m/s")

                # Get Icon
                icon_code = weather['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                self.update_icon(icon_url)
            else:
                self.city_name_label.configure(text="City Not Found")

        except Exception as e:
            self.city_name_label.configure(text="Error connecting...")

    def update_icon(self, url):
        response = requests.get(url)
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(100, 100))
        self.icon_label.configure(image=ctk_img)
        self.icon_label.image = ctk_img


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
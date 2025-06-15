import pygame
import json

with open("data/config/GUI.json", "r", encoding="utf-8") as f:
    config_GUI = json.load(f)

class Button():
    def __init__(self, x_pos: int, y_pos: int, width: int, height: int, text: str, color: list, action, font):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.text = text
        self.color = color
        self.action = action
        self.font = font
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius = 7)
        
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def on_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.action:
                self.action()
                return True
        return False

class MultilineText():
    def __init__(self, text, font):
        self.text = text
        self.font = font

    def draw(self, surface, x_pos, y_pos, width, config = config_GUI):
        self.lines = self.text.split("\n")
        height = (config["line_spacing"] * (len(self.lines) - 1) + 1) * config["font_size"]

        pygame.draw.rect(
            surface, 
            config["background_color"], 
            (x_pos, y_pos, width + 2 * config["padding"], height + 2 * config["padding"])
        )

        for line in self.lines:
            text_surface = self.font.render(line, True, config["text_color"])
            surface.blit(text_surface, (x_pos + config["padding"], y_pos + config["padding"]))
            y_pos += config["font_size"] * config["line_spacing"]

def draw_text(surface, text, font, x_pos, y_pos, width, config = config_GUI):
    lines = text.split("\n")
    height = (config["line_spacing"] * (len(lines) - 1) + 1) * config["font_size"]

    pygame.draw.rect(
        surface, 
        config["background_color"], 
        (x_pos, y_pos, width + 2 * config["padding"], height + 2 * config["padding"])
    )

    for line in lines:
        text_surface = font.render(line, True, config["text_color"])
        surface.blit(text_surface, (x_pos + config["padding"], y_pos + config["padding"]))
        y_pos += config["font_size"] * config["line_spacing"]
import pygame
import math
import sys

# Initialisation de Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 1400, 900
FPS = 60

# Couleurs (basées sur le CSS)
BG_COLOR = (15, 23, 42)  # slate-950
CYAN_400 = (34, 211, 238)
CYAN_300 = (103, 232, 249)
BLUE_400 = (96, 165, 250)
BLUE_500 = (59, 130, 246)
PURPLE_400 = (192, 132, 252)
SLATE_900 = (15, 23, 42)
SLATE_800 = (30, 41, 59)

# Définition des compétences (arbre simplifié)
SKILLS = {
    # Tier 1 - Base
    'core': {
        'id': 'core',
        'name': 'CORE SYSTEM',
        'description': 'Base neural processing',
        'cost': 0,
        'pos': (700, 210),
        'tier': 1,
        'dependencies': []
    },
    
    # Tier 2 - Branches principales
    'vision': {
        'id': 'vision',
        'name': 'VISION MODULE',
        'description': 'Enhanced optical sensors',
        'cost': 2,
        'pos': (400, 360),
        'tier': 2,
        'dependencies': ['core']
    },
    'processing': {
        'id': 'processing',
        'name': 'CPU BOOST',
        'description': 'Faster processing speed',
        'cost': 2,
        'pos': (700, 360),
        'tier': 2,
        'dependencies': ['core']
    },
    'mobility': {
        'id': 'mobility',
        'name': 'MOBILITY',
        'description': 'Improved movement',
        'cost': 2,
        'pos': (1000, 360),
        'tier': 2,
        'dependencies': ['core']
    },
    
    # Tier 3 - Spécialisations
    'ai_vision': {
        'id': 'ai_vision',
        'name': 'AI VISION',
        'description': 'Object recognition',
        'cost': 3,
        'pos': (300, 510),
        'tier': 3,
        'dependencies': ['vision']
    },
    'night_vision': {
        'id': 'night_vision',
        'name': 'NIGHT VISION',
        'description': 'See in darkness',
        'cost': 3,
        'pos': (500, 510),
        'tier': 3,
        'dependencies': ['vision']
    },
    'overclock': {
        'id': 'overclock',
        'name': 'OVERCLOCK',
        'description': 'Maximum performance',
        'cost': 4,
        'pos': (700, 510),
        'tier': 3,
        'dependencies': ['processing']
    },
    'turbo': {
        'id': 'turbo',
        'name': 'TURBO MODE',
        'description': 'Speed boost',
        'cost': 3,
        'pos': (900, 510),
        'tier': 3,
        'dependencies': ['mobility']
    },
    'flight': {
        'id': 'flight',
        'name': 'FLIGHT',
        'description': 'Aerial capabilities',
        'cost': 4,
        'pos': (1100, 510),
        'tier': 3,
        'dependencies': ['mobility']
    },
    
    # Tier 4 - Ultimate
    'quantum': {
        'id': 'quantum',
        'name': 'QUANTUM CORE',
        'description': 'Ultimate upgrade',
        'cost': 5,
        'pos': (700, 660),
        'tier': 4,
        'dependencies': ['overclock', 'ai_vision', 'turbo']
    }
}


class SkillNode:
    def __init__(self, skill_data):
        self.data = skill_data
        self.rect = pygame.Rect(0, 0, 160, 160)
        self.rect.center = skill_data['pos']
        self.hover = False
        self.particles = []
        
    def is_available(self, unlocked_skills):
        if self.data['id'] in unlocked_skills:
            return False
        for dep in self.data['dependencies']:
            if dep not in unlocked_skills:
                return False
        return True
    
    def is_unlocked(self, unlocked_skills):
        return self.data['id'] in unlocked_skills
    
    def draw(self, screen, unlocked_skills, skill_points, font, small_font):
        is_unlocked = self.is_unlocked(unlocked_skills)
        is_available = self.is_available(unlocked_skills)
        
            
        # Couleur du nœud
        if is_unlocked:
            color = CYAN_400
        elif is_available and skill_points >= self.data['cost']:
            color = BLUE_400
        elif is_available:
            color = (100, 120, 150)
        else:
            color = (50, 50, 70)
        
        
        # Choisir l'image hexagone selon le statut
        if is_unlocked:
            hex_img = pygame.image.load('assets/SkillTree/hexa_bought.png')
        elif is_available and skill_points >= self.data['cost']:
            hex_img = pygame.image.load('assets/SkillTree/hexa_canbuy.png')
        elif is_available:
            hex_img = pygame.image.load('assets/SkillTree/hexa_unlocked.png')
        else:
            hex_img = pygame.image.load('assets/SkillTree/hexa_locked.png')
        
        # Redimensionner et centrer l'hexagone
        hex_img = pygame.transform.scale(hex_img, (140, 151.5))
        hex_rect = hex_img.get_rect(center=self.rect.center)
        screen.blit(hex_img, hex_rect)
        
        # Icône tier
        tier_text = small_font.render(f"T{self.data['tier']}", True, color)
        tier_rect = tier_text.get_rect(center=(self.rect.centerx, self.rect.centery - 30))
        screen.blit(tier_text, tier_rect)
        
        # Nom
        name_lines = self.data['name'].split()
        y_offset = -10
        for line in name_lines:
            name_text = small_font.render(line, True, (255, 255, 255) if is_unlocked or is_available else (100, 100, 120))
            name_rect = name_text.get_rect(center=(self.rect.centerx, self.rect.centery + y_offset))
            screen.blit(name_text, name_rect)
            y_offset += 18
        
        # Coût
        if not is_unlocked:
            cost_text = small_font.render(f"{self.data['cost']} pts", True, 
                                        CYAN_300 if skill_points >= self.data['cost'] else (150, 150, 150))
            cost_rect = cost_text.get_rect(center=(self.rect.centerx, self.rect.centery + 35))
            screen.blit(cost_text, cost_rect)
        else:
            unlocked_text = small_font.render("Bought", True, CYAN_400)
            unlocked_rect = unlocked_text.get_rect(center=(self.rect.centerx, self.rect.centery + 35))
            screen.blit(unlocked_text, unlocked_rect)

        
        # Tooltip au survol
        if self.hover:
            self.draw_tooltip(screen, small_font)
    
    def draw_tooltip(self, screen, font):
        tooltip_width = 250
        tooltip_height = 80
        tooltip_x = 150
        tooltip_y = 150
        
        
        # Fond du tooltip
        tooltip_surface = pygame.Surface((tooltip_width, tooltip_height), pygame.SRCALPHA)
        pygame.draw.rect(tooltip_surface, (*SLATE_800, 240), (0, 0, tooltip_width, tooltip_height), border_radius=8)
        pygame.draw.rect(tooltip_surface, CYAN_400, (0, 0, tooltip_width, tooltip_height), 2, border_radius=8)
        
        # Texte
        desc_text = font.render(self.data['description'], True, (200, 200, 220))
        desc_rect = desc_text.get_rect(center=(tooltip_width // 2, tooltip_height // 2))
        tooltip_surface.blit(desc_text, desc_rect)
        
        screen.blit(tooltip_surface, (tooltip_x, tooltip_y))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("WALL·E Neural Upgrade Matrix")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Police
        self.title_font = pygame.font.Font(None, 48)
        self.font = pygame.font.Font(None, 28)
        self.small_font = pygame.font.Font(None, 18)
        
        # État du jeu
        self.skill_points = 10
        self.unlocked_skills = {'core'}  # Core débloqué par défaut
        
        # Nœuds de compétences
        self.skill_nodes = [SkillNode(skill) for skill in SKILLS.values()]
        
        # Animation
        self.pulse_time = 0
        
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEMOTION:
                for node in self.skill_nodes:
                    node.hover = node.rect.collidepoint(mouse_pos)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifier le bouton reset
                reset_rect = pygame.Rect(WIDTH // 2 - 100, 100, 200, 50)
                if reset_rect.collidepoint(mouse_pos):
                    self.skill_points = 10
                    self.unlocked_skills = {'core'}
                
                # Vérifier les nœuds de compétences
                for node in self.skill_nodes:
                    if node.rect.collidepoint(mouse_pos):
                        if node.is_available(self.unlocked_skills) and self.skill_points >= node.data['cost']:
                            self.skill_points -= node.data['cost']
                            self.unlocked_skills.add(node.data['id'])
    
    def draw_background(self):
        self.screen.fill(BG_COLOR)
        
        # Grille
        for x in range(0, WIDTH, 50):
            pygame.draw.line(self.screen, (20, 40, 60, 25), (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, 50):
            pygame.draw.line(self.screen, (20, 40, 60, 25), (0, y), (WIDTH, y), 1)
        
    
    def draw_ui(self):
        # Titre avec dégradé
        title_text = self.title_font.render("WALL·E NEURAL UPGRADE MATRIX", True, CYAN_400)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
        self.screen.blit(title_text, title_rect)
        
        # Ligne décorative
        pygame.draw.line(self.screen, CYAN_400, 
                        (WIDTH // 2 - 300, 55), (WIDTH // 2 + 300, 55), 1)
        
        # Statistiques
        points_text = self.font.render(f"UPGRADE POINTS: {self.skill_points}", True, CYAN_300)
        points_rect = points_text.get_rect(center=(WIDTH // 2 - 150, 80))
        self.screen.blit(points_text, points_rect)
        
        modules_text = self.font.render(f"ACTIVE MODULES: {len(self.unlocked_skills)}", True, BLUE_400)
        modules_rect = modules_text.get_rect(center=(WIDTH // 2 + 150, 80))
        self.screen.blit(modules_text, modules_rect)
        
        # Bouton reset
        reset_rect = pygame.Rect(WIDTH // 2 - 100, 100, 200, 40)
        mouse_pos = pygame.mouse.get_pos()
        reset_hover = reset_rect.collidepoint(mouse_pos)
        
        pygame.draw.rect(self.screen, SLATE_900, reset_rect, border_radius=8)
        pygame.draw.rect(self.screen, CYAN_400 if reset_hover else (100, 150, 180), 
                        reset_rect, 2, border_radius=8)
        
        reset_text = self.small_font.render("// RESET MATRIX", True, CYAN_400)
        reset_text_rect = reset_text.get_rect(center=reset_rect.center)
        self.screen.blit(reset_text, reset_text_rect)

    # Dessiner les connexions
    def draw_connections(self):
        for node in self.skill_nodes:
            for dep_id in node.data['dependencies']:
                dep_skill = SKILLS[dep_id]
                start_pos = dep_skill['pos']
                end_pos = node.data['pos']
            
                if node.is_unlocked(self.unlocked_skills):
                    color = CYAN_400
                    width = 3
                elif dep_id in self.unlocked_skills:
                    color = BLUE_400
                    width = 2
                else:
                    color = (50, 50, 70)
                    width = 1
                
                pygame.draw.line(self.screen, color, start_pos, end_pos, width)
    
    def run(self):
        while self.running:
            self.handle_events()
            
            
            self.draw_background()

            self.draw_connections()
            
            # Dessiner les nœuds de compétences
            for node in self.skill_nodes:
                node.draw(self.screen,
                self.unlocked_skills,
                self.skill_points,
                self.font,
                self.small_font
                )
            
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(FPS)
            self.pulse_time += 0.05
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
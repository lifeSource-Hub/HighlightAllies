import sys
import Level

MAIN_MODULE = sys.modules["__main__"]
SPRITE_SIZE = MAIN_MODULE.SPRITE_SIZE
old_draw_threat = MAIN_MODULE.PyGameView.draw_threat

def draw_threat_redux(self):
    old_draw_threat(self)

    lvl = self.get_display_level()
    img = MAIN_MODULE.get_image(['HighlightAllies', 'ally_highlight'])
    blit_area = (0, 0, SPRITE_SIZE, SPRITE_SIZE)
    to_blit = []

    if not isinstance(self.examine_target, Level.Unit):
        for unit in lvl.units:
            if not Level.are_hostile(self.game.p1, unit) and not unit.is_player_controlled:
                x = unit.x * SPRITE_SIZE
                y = unit.y * SPRITE_SIZE
                to_blit.append((img, (x, y), blit_area))

    self.level_display.blits(to_blit)

MAIN_MODULE.PyGameView.draw_threat = draw_threat_redux
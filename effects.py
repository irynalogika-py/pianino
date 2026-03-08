from pygame import draw, transform, image
# from settings import BLACK

# Картинки нот
C_IMG = transform.scale(image.load('assets/images/notes/c.png'), (50, 50))
D_IMG = transform.scale(image.load('assets/images/notes/d.png'), (50, 50))
E_IMG = transform.scale(image.load('assets/images/notes/e.png'), (50, 50))
A_IMG = transform.scale(image.load('assets/images/notes/a.png'), (50, 50))

NOTES_IMAGES = {
    'C': C_IMG,
    'D': D_IMG,
    'E': E_IMG,
    'A': A_IMG
}

_FLYING_NOTES = []


def spawn_flying_note(rect, note_name: str | None):
    if not note_name:
        return
    img = NOTES_IMAGES.get(note_name)
    if not img:
        return
    x = rect.centerx - img.get_width() // 2
    y = rect.y - img.get_height() - 10
    _FLYING_NOTES.append({'img': img, 'x': x, 'y': y, 'vy': -1})


def update_and_draw_flying_notes(screen):
    to_remove = []
    for note in _FLYING_NOTES:
        note['y'] += note['vy']
        screen.blit(note['img'], (note['x'], note['y']))
        if note['y'] + note['img'].get_height() < 0:
            to_remove.append(note)
    for note in to_remove:
        _FLYING_NOTES.remove(note)


# def draw_key_effect(screen, rect, is_pressed=False, note=None):
#     if not is_pressed:
#         base_color = (220, 0, 0)
#     else:
#         base_color = (0, 220, 255)
#
#     draw.rect(screen, base_color, rect, border_radius=8)
#     draw.rect(screen, BLACK, rect, 2, border_radius=8)

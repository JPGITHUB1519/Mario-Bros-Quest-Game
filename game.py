import pygame
import random
import sys
import time

class Player(pygame.sprite.Sprite) :

	def __init__(self) :

		imagen = pygame.image.load("mario.png")
		self.image = imagen
		#get width and height
		self.rect = self.image.get_rect()
		self.rect.left = 0
		self.rect.top = 0

	def update(self, pantalla) :

		pantalla.blit(self.image, self.rect)

	def mover(self,x,y) :

		self.rect.move_ip(x,y)

	def colision(self, lista,cond_gameover) :

		colisiono = False

		for i in lista :
			if mario.rect.colliderect(i) :

				mario.rect.left = xant
				mario.rect.top = yant
				colisiono = True
				cond_gameover = True

		return colisiono,cond_gameover



	def colision_bonus(self, lista, score,channel,sound,bad_sound):


		for i in lista :

			if mario.rect.colliderect(i.rect) :

				score += i.score
				# remove from the screen
				lista.remove(i)
				#if collision is bad mushroom play bad

				if i.num_image == 3 :
					channel.play(bad_sound)
				else :
					channel.play(sound)

		return score

		

		

	def screen_colition(self, xsize, ysize) :

		if self.rect.top < 0 :

			return True

		if self.rect.left < 0 :

			return True

		if self.rect.left >= xsize - 50 :

			return True


		if self.rect.top >= ysize - 60 :

			return True

	def door_colision(self, door) :

		if self.rect.colliderect(door) :

			return True

		return False

class Sprite(pygame.sprite.Sprite) :

	def __init__(self,imagen, x, y) :

		self.image = imagen
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y

	def update(self, pantalla) :

		pantalla.blit(self.image, self.rect)



class Enemy(pygame.sprite.Sprite) :

	def __init__ (self,x, y) :

		# storing the images
		imagenes = []
		imagenes.append(pygame.image.load("enemy.png"))
		imagenes.append(pygame.image.load("bowser.png"))
		imagenes.append(pygame.image.load("goomba.png"))
		imagenes.append(pygame.image.load("boo.png"))
		imagenes.append(pygame.image.load("blooper.png"))

		# random number to select a random image
		num_image = random.randint(0, len(imagenes) - 1)
		self.image = imagenes[num_image]
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x, y

	def update(self, pantalla) :

		pantalla.blit(self.image, self.rect)

class Bonus(pygame.sprite.Sprite) :

	def __init__(self, x, y) :

		imagenes = ["mushroom.png",  "blue_mushroom.png", "green_mushroom.png", "bad_mushroom_ghost.png"]
		self.num_image = random.randint(0, len(imagenes) - 1)

		self.image = pygame.image.load(imagenes[self.num_image])
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y

		self.score = self.set_mushroom_value(self.num_image, imagenes)

	

	def set_mushroom_value(self,num_image,mushrooms) :

		if num_image == 0 :

			return 1

		if num_image == 1 :

			return 3

		if num_image == 2 :

			return 5
		
		if num_image == 3 :

			return -1


	def update(self, pantalla) :

		pantalla.blit(self.image, self.rect)


def create_enemy_list(lista, cantidad, player, lista_bonus) :

	# the problem was the cicle

	# the new functions draw the objects without collisions
	for i in range(0, cantidad) :
		collide = True

		while collide == True : 
			xrand = random.randint(100,600)
			yrand = random.randint(0,400)
			objeto = Enemy(xrand, yrand)

			cond = 0
			for j in lista :
				if objeto.rect.colliderect(j.rect) or objeto.rect.colliderect(player.rect):
					cond = 1
					break

			# check if collide with bonus
			for j in lista_bonus :
				if objeto.rect.colliderect(j.rect) :
					cond = 1
					break
			if cond == 0 :
				lista.append(objeto)
				collide = False


def create_bonus_list(lista, cantidad, player) :

	# the problem was the cicle

	# the new functions draw the objects without collisions
	for i in range(0, cantidad) :
		collide = True

		while collide == True : 
			xrand = random.randint(100,600)
			yrand = random.randint(0,400)
			objeto = Bonus(xrand, yrand)

			cond = 0
			for j in lista :
				if objeto.rect.colliderect(j.rect) or objeto.rect.colliderect(player.rect):
					cond = 1
					break
			if cond == 0 :
				lista.append(objeto)
				collide = False

def text_to_screen(texto,x,y) :

	pantalla.blit(texto, (x,y))



def show_sprite_list(lista, pantalla) :

	for i in range(0, len(lista)) :

		lista[i].update(pantalla)



class Cursor(pygame.Rect) :

	def __init__(self) :

		pygame.Rect.__init__(self, 0,0,0,1)

	def update(self) :

		self.left, self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite) :

	def __init__(self, imagen1, imagen2, x = 200, y = 200) :

		self.imagen_normal = imagen1
		self.imagen_seleccion = imagen2
		self.rect = self.imagen_normal.get_rect()
		self.rect.left, self.rect.top = x,y 
		self.imagen_actual = self.imagen_normal

	def update(self, pantalla, cursor) :

		if cursor.colliderect(self.rect) :

			self.imagen_actual = self.imagen_normal

		else :

			self.imagen_actual = self.imagen_seleccion

		pantalla.blit(self.imagen_actual, self.rect)

def show_menu(pantalla,cursor,botones) :

	for button in botones :

		button.update(pantalla, cursor)

	fuente1 = pygame.font.Font("Pacifico.ttf",45)

	texto_titulo = fuente1.render("Mario Bros Quest",0,(0,0,255))

	text_to_screen(texto_titulo, 250,35)

	image_title = pygame.image.load("title.jpg")

	pantalla.blit(image_title, (300,150))

	cursor.update()


def show_gameover() :

	fuente = pygame.font.Font("game_over.ttf",60)
	texto_congrats = fuente.render("Game Over, Pulsa Espacio Para Jugar de nuevo",0,(255,0,0))

	text_to_screen(texto_congrats,150,200)


def show_congratulation(puntacion, max_puntuacion) :

	fuente = pygame.font.Font("Impregnable.ttf",45)
	fuente2 = pygame.font.SysFont("Arial",45)
	fuente3 = pygame.font.SysFont("Arial",30)

	if puntuacion > max_puntuacion :
		save_max_score("data.txt", str(puntuacion))
		texto_max_puntuacion = fuente.render("Has Conseguido la Maxima Puntacion!....",0,(128,0,128))
		text_to_screen(texto_max_puntuacion,150,150)
	texto_congratulations = fuente.render("Felicidades, Has Ganado!",0,(255,0,0))
	texto_puntacion = fuente2.render("Tu Puntuacion es : " + str(puntacion),0,(255,0,0))
	texto_tecla = fuente3.render("Pulsa Espacio para Jugar de Nuevo",0,(0,0,255))
	text_to_screen(texto_congratulations,150,200)
	text_to_screen(texto_puntacion,150,250)
	text_to_screen(texto_tecla,150,350)

# score functions

def get_max_score(filename) :

	file = open(filename,"r")
	content = file.readline()
	return content

def save_max_score(filename,score) :

	file = open(filename, "r+")
	file.write(score)

def check_sound(sonido, cond) :

	if cond == False :

		sonido.play()

	cond = True

	return cond


pygame.init()

xsize = 800
ysize = 500
image_game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(image_game_icon)
pantalla = pygame.display.set_mode([xsize,ysize])


reloj = pygame.time.Clock()
mario = Player()
imagen_door = pygame.image.load("door.png")
door = Sprite(imagen_door, 700,400)
salir = False

lista_bonus = []
create_bonus_list(lista_bonus,5, mario)

lista = []
create_enemy_list(lista,5, mario, lista_bonus)

#sounds

sound_mushroom = pygame.mixer.Sound("mushroom.wav")
sound_bad_mushroom = pygame.mixer.Sound("bad_mushroom.wav")
sound_gameover = pygame.mixer.Sound("game_over.wav")
sound_stage_clear = pygame.mixer.Sound("stage_clear.wav")
sound_best_score = pygame.mixer.Sound("best_score.wav")


# channel to play game over sound
channel_sounds = pygame.mixer.Channel(5)
cond_music_title = False
cond_music_game = False
cond_sound_mushroom = False
cond_sound_gameover = False
cond_sound_stage_clear = False
cond_sound_best_score = False
cond_sound_bad_mushroom = False


#bonus


hongo = Bonus(150,150)

downsigueapretada = False
upsigueapretada = False
leftsigueapretada = False
rightsigueapretada = False
vx = 0
vy = 0
velocidad = 10
colisiono = False

# fonts

fuente1 = pygame.font.SysFont("Arial", 25)


# aux

puntuacion = 0
max_puntuacion = get_max_score("data.txt")
max_puntuacion = int(max_puntuacion)
timer = 0

# menu variables

cursor1 = Cursor()
boton1_imagen_normal = pygame.image.load("jugar.png")
boton1_imagen_seleccion = pygame.image.load("jugar_sel.png")
boton2_imagen_normal = pygame.image.load("salir.png")
boton2_imagen_seleccion = pygame.image.load("salir_sel.png")
boton1 = Boton(boton1_imagen_normal, boton1_imagen_seleccion, 250,400)
boton2 = Boton(boton2_imagen_normal, boton2_imagen_seleccion,450,400)

#conds

cond_menu = True
cond_juego = False	
cond_gameover = False
cond_congratulations = False


"""
y = 20
for i in range(0, 5) : 
	lista.append(Enemy(imagen, 0, y))
	y += 20
"""

while salir != True :

	for event in pygame.event.get() :

		if event.type == pygame.QUIT :

			salir = True

		if colisiono == False :
			if event.type == pygame.KEYDOWN :

				if event.key == pygame.K_LEFT :

					leftsigueapretada = True
					vx = -velocidad

				if event.key == pygame.K_RIGHT :

					rightsigueapretada = True
					vx =  velocidad

				if event.key == pygame.K_UP :

					upsigueapretada = True
					vy = - velocidad

				if event.key == pygame.K_DOWN :

					downsigueapretada = True
					vy = velocidad

			if event.type == pygame.KEYUP :

				if event.key == pygame.K_LEFT :

					leftsigueapretada = False

					if rightsigueapretada :
						vx = velocidad
					else :
						vx = 0

				if event.key == pygame.K_RIGHT :

					rightsigueapretada = False

					if leftsigueapretada :
						vx = - velocidad
					else :
						vx = 0

				if event.key == pygame.K_UP :

					upsigueapretada = False

					if downsigueapretada :
						vy = velocidad
					else :
						vy = 0

				if event.key == pygame.K_DOWN :

					downsigueapretada = False

					if upsigueapretada :
						vy = - velocidad
					else :
						vy = 0

			if event.type == pygame.MOUSEBUTTONDOWN :

				# actions buttons menu
				if cursor1.colliderect(boton1) :
					
					if cond_juego == False :
						# start counter
						start_time = time.time()
					cond_menu = False
					cond_juego = True
					

				if cursor1.colliderect(boton2) :

					pygame.quit()
					# salir del programa
					sys.exit(0)

		# condition to continue playing after gameover
		if (cond_gameover == True or cond_congratulations) and cond_juego == False :

			if event.type == pygame.KEYDOWN :

				if event.key == pygame.K_SPACE :

					cond_juego = True
					if cond_gameover == True :
						cond_gameover = False

					if cond_congratulations == True :
						cond_congratulations = False

					#restart music
					pygame.mixer.music.rewind()
					pygame.mixer.music.play()
					# restar sounds
					cond_sound_gameover = False
					cond_sound_stage_clear = False
					cond_sound_best_score = False

					# check if the channel's sound is not actually playing. if it is stop the sound
					if channel_sounds.get_busy() == True :

						channel_sounds.stop()

					# restart all
					mario = Player()
					vx, vy = 0,0
					lista_bonus = []
					create_bonus_list(lista_bonus,5, mario)
					lista = []
					create_enemy_list(lista,5, mario, lista_bonus)
					puntuacion = 0
					max_puntuacion = get_max_score("data.txt")
					max_puntuacion = int(max_puntuacion)
					# reset time
					start_time = time.time()
					aux_time = time.time()


	reloj.tick(20)
	pantalla.fill((255,255,255))

	if cond_menu == True :

		show_menu(pantalla, cursor1, [boton1, boton2])
		if cond_music_title == False :
			pygame.mixer.music.load("title.mp3")
			pygame.mixer.music.play(-1)
			cond_music_title = True

	if cond_juego == True :

		if cond_music_game == False :
			pygame.mixer.music.load("game.ogg")
			pygame.mixer.music.play(-1)
			cond_music_game = True
		xant, yant = mario.rect.left, mario.rect.top
		mario.mover(vx,vy)
		door.update(pantalla)



		# screen colition
		if mario.screen_colition(xsize, ysize) == True :

			mario.rect.left, mario.rect.top = xant, yant

		# door collision
		if mario.door_colision(door) == True :

			cond_congratulations = True

		colisiono,cond_gameover = mario.colision(lista,cond_gameover)

		# count time
		if colisiono == False :
			#time = pygame.time.get_ticks() / 1000
			aux_time = time.time()
			timer = int(aux_time - start_time)
		# showing sprites
		mario.update(pantalla)
		show_sprite_list(lista, pantalla)
		show_sprite_list(lista_bonus, pantalla)

		puntuacion = mario.colision_bonus(lista_bonus, puntuacion, channel_sounds, sound_mushroom, sound_bad_mushroom)

		texto_puntuacion = fuente1.render("Puntuacion : " + str(puntuacion),0,(0,0,0))
		texto_time = fuente1.render("Tiempo : " + str(timer),0,(0,0,0))
		texto_max_puntuacion = fuente1.render("Max Punt. : " + str(max_puntuacion),0,(0,0,0))
		text_to_screen(texto_puntuacion, 630,0)
		text_to_screen(texto_time, 650,40)
		text_to_screen(texto_max_puntuacion,650,80)
		
	if cond_gameover == True :

		pygame.mixer.music.stop()

		if cond_sound_gameover == False :
			channel_sounds.play(sound_gameover)
			cond_sound_gameover = True
		show_gameover()
		cond_juego = False

	if cond_congratulations == True :

		if puntuacion > max_puntuacion :
			if cond_sound_best_score == False :

				channel_sounds.play(sound_best_score)
				cond_sound_best_score = True
		else :

			if cond_sound_stage_clear == False :
				channel_sounds.play(sound_stage_clear)
				cond_sound_stage_clear = True
		pygame.mixer.music.stop()
		cond_juego = False
		show_congratulation(puntuacion, max_puntuacion)
			
	pygame.display.update()

pygame.quit()

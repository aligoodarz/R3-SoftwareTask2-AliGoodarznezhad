
# importing pygame module
import socket
import pygame

# importing sys module
import sys


# creating a running loop
def get_key():

    # initialising pygame
    pygame.init()

    # creating display
    display = pygame.display.set_mode((300, 300))

    keys_pressed = []
    # number 1 is up
    # number 2 is down
    # number 3 is right
    # number 4 is left
    while True:
        # creating a loop to check events that
        # are occuring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:

                # checking if key "A" was pressed
                if event.key == pygame.K_UP:
                    print("Key UP has been pressed")
                    return 1

                # checking if key "J" was pressed
                if event.key == pygame.K_DOWN:
                    print("Key DOWN has been pressed")
                    return 2
                # checking if key "P" was pressed
                if event.key == pygame.K_RIGHT:
                    print("Key RIGHT has been pressed")
                    return 3

                # checking if key "M" was pressed
                if event.key == pygame.K_LEFT:
                    print("Key LEFT has been pressed")
                    return 4

                if event.key == pygame.K_ESCAPE:
                    break


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
    input_given = get_key()
    s.send(input_given.to_bytes(2, 'big'))

    data = s.recv(BUFFER_SIZE)
    print("received data:", data)

s.close()

package entity;

import main.GamePanel;
import main.KeyHandler;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;

public class Player extends Entity {
    GamePanel gp;
    KeyHandler keyHandler;
    public final int screenX, screenY;

    public Player(GamePanel gp, KeyHandler keyHandler) {

        this.gp = gp;
        this.keyHandler = keyHandler;

        this.screenX = gp.screenWidth / 2 - (gp.tileSize / 2);
        this.screenY = gp.screenHeight / 2 - (gp.tileSize / 2);

        this.solidArea = new Rectangle();
        this.solidArea.x = 8;
        this.solidArea.y = 16;
        this.solidArea.width = 32;
        this.solidArea.height = 32;

        this.setDefaultValues();
        this.getPlayerImage();

    }
    public void setDefaultValues () {
        this.worldX = gp.tileSize * 23;
        this.worldY = gp.tileSize * 21;
        this.speed = 4;
        this.direction = "down";
    }
    public void getPlayerImage() {

        try {
            up1 = ImageIO.read(getClass().getResourceAsStream("/player/boy_up_1.png"));
            up2 = ImageIO.read(getClass().getResourceAsStream("/player/boy_up_2.png"));
            down1 = ImageIO.read(getClass().getResourceAsStream("/player/boy_down_1.png"));
            down2 = ImageIO.read(getClass().getResourceAsStream("/player/boy_down_2.png"));
            left1 = ImageIO.read(getClass().getResourceAsStream("/player/boy_left_1.png"));
            left2 = ImageIO.read(getClass().getResourceAsStream("/player/boy_left_2.png"));
            right1 = ImageIO.read(getClass().getResourceAsStream("/player/boy_right_1.png"));
            right2 = ImageIO.read(getClass().getResourceAsStream("/player/boy_right_2.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public void update () {
        if (keyHandler.upPressed ||
            keyHandler.downPressed ||
            keyHandler.leftPressed ||
            keyHandler.rightPressed) {

            if (keyHandler.upPressed) {
                this.direction = "up";
                this.worldY -= this.speed;
            }
            if (keyHandler.downPressed) {
                this.direction = "down";
                this.worldY += this.speed;
            }
            if (keyHandler.leftPressed) {
                this.direction = "left";
                this.worldX -= this.speed;
            }
            if (keyHandler.rightPressed) {
                this.direction = "right";
                this.worldX += this.speed;
            }

            collisionOn = false;
            gp.cChecker.checkTile(this);

            spriteCounter++;
            if (spriteCounter > 10) {
                if (spriteNum == 1) {
                    spriteNum = 2;
                } else spriteNum = 1;
                spriteCounter = 0;
            }
        }

    }
    public void draw (Graphics2D g2) {
        //g2.setColor(Color.white);
        //g2.fillRect(this.x, this.y, gp.tileSize, gp.tileSize);
        BufferedImage image = null;
        switch (this.direction) {
            case "up":
                if (this.spriteNum == 1) {
                    image = up1;
                }
                if (this.spriteNum == 2) {
                    image = up2;
                }
                break;
            case "down":
                if (this.spriteNum == 1) {
                    image = down1;
                }
                if (this.spriteNum == 2) {
                    image = down2;
                }
                break;
            case "left":
                if (this.spriteNum == 1) {
                    image = left1;
                }
                if (this.spriteNum == 2) {
                    image = left2;
                }
                break;
            case "right":
                if (this.spriteNum == 1) {
                    image = right1;
                }
                if (this.spriteNum == 2) {
                    image = right2;
                }
                break;
        }
        g2.drawImage(image, this.screenX, this.screenY, gp.tileSize, gp.tileSize, null);
    }
}

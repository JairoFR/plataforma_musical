-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_plataforma
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `db_plataforma` ;

-- -----------------------------------------------------
-- Schema db_plataforma
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_plataforma` DEFAULT CHARACTER SET utf8mb3 ;
USE `db_plataforma` ;

-- -----------------------------------------------------
-- Table `db_plataforma`.`artistas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`artistas` (
  `artistas_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`artistas_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`info_artistas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`info_artistas` (
  `info_artistas_id` INT NOT NULL AUTO_INCREMENT,
  `artistas_id` INT NOT NULL,
  `año_formacion` INT NULL DEFAULT NULL,
  `biografia` TEXT NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`info_artistas_id`),
  INDEX `fk_info_artistas_artistas1_idx` (`artistas_id` ASC) VISIBLE,
  CONSTRAINT `fk_info_artistas_artistas1`
    FOREIGN KEY (`artistas_id`)
    REFERENCES `db_plataforma`.`artistas` (`artistas_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`canciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`canciones` (
  `cancion_id` INT NOT NULL AUTO_INCREMENT,
  `artista_id` INT NOT NULL,
  `cancion1` VARCHAR(255) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`cancion_id`),
  INDEX `fk_canciones_artistas1_idx` (`artista_id` ASC) VISIBLE,
  CONSTRAINT `fk_canciones_artistas1`
    FOREIGN KEY (`artista_id`)
    REFERENCES `db_plataforma`.`info_artistas` (`info_artistas_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`promociones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`promociones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `imagen` VARCHAR(255) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`comentarios_artists`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`comentarios_artists` (
  `comentarios_artists_id` INT NOT NULL AUTO_INCREMENT,
  `artistas_id` INT NOT NULL,
  `promociones_id` INT NOT NULL,
  `comentarios` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`comentarios_artists_id`),
  INDEX `fk_comentarios_artists_artistas1_idx` (`artistas_id` ASC) VISIBLE,
  INDEX `fk_comentarios_artists_promociones1_idx` (`promociones_id` ASC) VISIBLE,
  CONSTRAINT `fk_comentarios_artists_artistas1`
    FOREIGN KEY (`artistas_id`)
    REFERENCES `db_plataforma`.`artistas` (`artistas_id`),
  CONSTRAINT `fk_comentarios_artists_promociones1`
    FOREIGN KEY (`promociones_id`)
    REFERENCES `db_plataforma`.`promociones` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`usuarios` (
  `usuarios_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`usuarios_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`comentarios_usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`comentarios_usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuarios_id` INT NOT NULL,
  `promociones_id` INT NOT NULL,
  `comentario` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comentarios_usuarios_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  INDEX `fk_comentarios_usuarios_promociones1_idx` (`promociones_id` ASC) VISIBLE,
  CONSTRAINT `fk_comentarios_usuarios_promociones1`
    FOREIGN KEY (`promociones_id`)
    REFERENCES `db_plataforma`.`promociones` (`id`),
  CONSTRAINT `fk_comentarios_usuarios_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `db_plataforma`.`usuarios` (`usuarios_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`date_eventos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`date_eventos` (
  `date_eventos_id` INT NOT NULL AUTO_INCREMENT,
  `artistas_id` INT NOT NULL,
  `nombre_evento` VARCHAR(255) NULL,
  `fecha` DATE NULL DEFAULT NULL,
  `hora` TIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`date_eventos_id`),
  INDEX `fk_date_eventos_artistas1_idx` (`artistas_id` ASC) VISIBLE,
  CONSTRAINT `fk_date_eventos_artistas1`
    FOREIGN KEY (`artistas_id`)
    REFERENCES `db_plataforma`.`artistas` (`artistas_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`paises`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`paises` (
  `pais_id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`pais_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`regiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`regiones` (
  `region_id` INT NOT NULL AUTO_INCREMENT,
  `pais_id` INT NOT NULL,
  `nombre` VARCHAR(255) NULL DEFAULT NULL,
  `created_At` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`region_id`),
  INDEX `fk_regiones_paises_idx` (`pais_id` ASC) VISIBLE,
  CONSTRAINT `fk_regiones_paises`
    FOREIGN KEY (`pais_id`)
    REFERENCES `db_plataforma`.`paises` (`pais_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`ciudades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`ciudades` (
  `id_ciudad` INT NOT NULL AUTO_INCREMENT,
  `region_id` INT NOT NULL,
  `pais_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `created_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id_ciudad`),
  INDEX `fk_ciudades_regiones1_idx` (`region_id` ASC) VISIBLE,
  INDEX `fk_ciudades_paises1_idx` (`pais_id` ASC) VISIBLE,
  CONSTRAINT `fk_ciudades_regiones1`
    FOREIGN KEY (`region_id`)
    REFERENCES `db_plataforma`.`regiones` (`region_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ciudades_paises1`
    FOREIGN KEY (`pais_id`)
    REFERENCES `db_plataforma`.`paises` (`pais_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_plataforma`.`direcciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`direcciones` (
  `direcciones_id` INT NOT NULL AUTO_INCREMENT,
  `artistas_id` INT NULL DEFAULT NULL,
  `date_eventos_id` INT NULL DEFAULT NULL,
  `usuarios_id` INT NULL DEFAULT NULL,
  `id_ciudad` INT NOT NULL,
  `region_id` INT NOT NULL,
  `pais_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`direcciones_id`),
  INDEX `fk_direcciones_ciudades1_idx` (`id_ciudad` ASC) VISIBLE,
  INDEX `fk_direcciones_regiones1_idx` (`region_id` ASC) VISIBLE,
  INDEX `fk_direcciones_paises1_idx` (`pais_id` ASC) VISIBLE,
  INDEX `fk_direcciones_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  INDEX `fk_direcciones_date_eventos1_idx` (`date_eventos_id` ASC) VISIBLE,
  INDEX `fk_direcciones_artistas1_idx` (`artistas_id` ASC) VISIBLE,
  CONSTRAINT `fk_direcciones_ciudades1`
    FOREIGN KEY (`id_ciudad`)
    REFERENCES `db_plataforma`.`ciudades` (`id_ciudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_direcciones_regiones1`
    FOREIGN KEY (`region_id`)
    REFERENCES `db_plataforma`.`regiones` (`region_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_direcciones_paises1`
    FOREIGN KEY (`pais_id`)
    REFERENCES `db_plataforma`.`paises` (`pais_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_direcciones_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `db_plataforma`.`usuarios` (`usuarios_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_direcciones_date_eventos1`
    FOREIGN KEY (`date_eventos_id`)
    REFERENCES `db_plataforma`.`date_eventos` (`date_eventos_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_direcciones_artistas1`
    FOREIGN KEY (`artistas_id`)
    REFERENCES `db_plataforma`.`artistas` (`artistas_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`fotos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`fotos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `info_artistas_id` INT NOT NULL,
  `image1` VARCHAR(255) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_fotos_info_artistas1_idx` (`info_artistas_id` ASC) VISIBLE,
  CONSTRAINT `fk_fotos_info_artistas1`
    FOREIGN KEY (`info_artistas_id`)
    REFERENCES `db_plataforma`.`info_artistas` (`info_artistas_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`generos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`generos` (
  `genero_id` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`genero_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`generos_musicales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`generos_musicales` (
  `artista_id` INT NOT NULL,
  `genero_id` INT NOT NULL,
  PRIMARY KEY (`artista_id`, `genero_id`),
  INDEX `fk_artistas_has_generos_musicales_generos_musicales1_idx` (`genero_id` ASC) VISIBLE,
  INDEX `fk_artistas_has_generos_musicales_artistas1_idx` (`artista_id` ASC) VISIBLE,
  CONSTRAINT `fk_artistas_has_generos_musicales_artistas1`
    FOREIGN KEY (`artista_id`)
    REFERENCES `db_plataforma`.`info_artistas` (`info_artistas_id`),
  CONSTRAINT `fk_artistas_has_generos_musicales_generos_musicales1`
    FOREIGN KEY (`genero_id`)
    REFERENCES `db_plataforma`.`generos` (`genero_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`seguidores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`seguidores` (
  `usuarios_id` INT NOT NULL,
  `artistas_id` INT NOT NULL,
  PRIMARY KEY (`usuarios_id`, `artistas_id`),
  INDEX `fk_usuarios_has_artistas_artistas1_idx` (`artistas_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_artistas_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_artistas_artistas1`
    FOREIGN KEY (`artistas_id`)
    REFERENCES `db_plataforma`.`artistas` (`artistas_id`),
  CONSTRAINT `fk_usuarios_has_artistas_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `db_plataforma`.`usuarios` (`usuarios_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`sociales_band`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`sociales_band` (
  `social_band_id` INT NOT NULL AUTO_INCREMENT,
  `info_artistas_id` INT NOT NULL,
  `facebook` VARCHAR(255) NULL DEFAULT NULL,
  `youtube` VARCHAR(255) NULL DEFAULT NULL,
  `instagram` VARCHAR(255) NULL DEFAULT NULL,
  `spotify` VARCHAR(255) NULL DEFAULT NULL,
  `apple_music` VARCHAR(255) NULL DEFAULT NULL,
  `amazon_music` VARCHAR(255) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`social_band_id`),
  INDEX `fk_sociales_band_info_artistas1_idx` (`info_artistas_id` ASC) VISIBLE,
  CONSTRAINT `fk_sociales_band_info_artistas1`
    FOREIGN KEY (`info_artistas_id`)
    REFERENCES `db_plataforma`.`info_artistas` (`info_artistas_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `db_plataforma`.`integrantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_plataforma`.`integrantes` (
  `integrantes_id` INT NOT NULL,
  `info_artistas_id` INT NOT NULL,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `instrumento` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`integrantes_id`),
  INDEX `fk_integrantes_info_artistas1_idx` (`info_artistas_id` ASC) VISIBLE,
  CONSTRAINT `fk_integrantes_info_artistas1`
    FOREIGN KEY (`info_artistas_id`)
    REFERENCES `db_plataforma`.`info_artistas` (`info_artistas_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

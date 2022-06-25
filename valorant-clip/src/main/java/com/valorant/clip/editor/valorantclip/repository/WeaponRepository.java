package com.valorant.clip.editor.valorantclip.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.valorant.clip.editor.valorantclip.model.Weapon;

@Repository
public interface WeaponRepository  extends JpaRepository<Weapon, Integer> {

}

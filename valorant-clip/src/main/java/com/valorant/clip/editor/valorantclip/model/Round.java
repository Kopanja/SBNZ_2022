package com.valorant.clip.editor.valorantclip.model;

public class Round {

	private int roundNumber = 0;
	private int teamAlive = 5;
	private int enemyAlive = 5;
	
	
	public int getRoundNumber() {
		return roundNumber;
	}
	public void setRoundNumber(int roundNumber) {
		this.roundNumber = roundNumber;
	}
	public int getTeamAlive() {
		return teamAlive;
	}
	public void setTeamAlive(int teamAlive) {
		this.teamAlive = teamAlive;
	}
	public int getEnemyAlive() {
		return enemyAlive;
	}
	public void setEnemyAlive(int enemyAlive) {
		this.enemyAlive = enemyAlive;
	}

	
}

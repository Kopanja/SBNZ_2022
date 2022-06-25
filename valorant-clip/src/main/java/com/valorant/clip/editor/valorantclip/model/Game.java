package com.valorant.clip.editor.valorantclip.model;

import java.util.List;
import org.kie.api.definition.type.PropertyReactive;

@PropertyReactive
public class Game {

	private List<String> myTeam;
	private List<String> enemyTeam;
	private String myAgent;
	private int roundsWon;
	private int roundsLost;
	
	
	public Game() {
		super();
	}
	public Game(List<String> myTeam, List<String> enemyTeam, String myAgent) {
		super();
		this.myTeam = myTeam;
		this.enemyTeam = enemyTeam;
		this.myAgent = myAgent;
	}
	public List<String> getMyTeam() {
		return myTeam;
	}
	public void setMyTeam(List<String> myTeam) {
		this.myTeam = myTeam;
	}
	public List<String> getEnemyTeam() {
		return enemyTeam;
	}
	public void setEnemyTeam(List<String> enemyTeam) {
		this.enemyTeam = enemyTeam;
	}
	public String getMyAgent() {
		return myAgent;
	}
	public void setMyAgent(String myAgent) {
		this.myAgent = myAgent;
	}
	
	public void incrRoundsWon() {
		this.roundsWon = this.roundsWon + 1;
	}
	
	public void incrRoundsLost() {
		this.roundsLost = this.roundsLost + 1;
	}
	
	public int getRoundsWon() {
		return roundsWon;
	}
	public void setRoundsWon(int roundsWon) {
		this.roundsWon = roundsWon;
	}
	public int getRoundsLost() {
		return roundsLost;
	}
	public void setRoundsLost(int roundsLost) {
		this.roundsLost = roundsLost;
	}
	@Override
	public String toString() {
		return "Game [myTeam=" + myTeam + ", enemyTeam=" + enemyTeam + ", myAgent=" + myAgent + ", roundsWon="
				+ roundsWon + ", roundsLost=" + roundsLost + "]";
	}
	
	
	
}

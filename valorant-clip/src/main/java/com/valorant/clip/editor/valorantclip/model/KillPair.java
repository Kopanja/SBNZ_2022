package com.valorant.clip.editor.valorantclip.model;

import org.kie.api.definition.type.Position;

public class KillPair {

	@Position(0)
	private Kill previousKill;
	
	@Position(1)
	private Kill nextKill;

	public KillPair() {
		super();
	}

	public KillPair(Kill previousKill, Kill nextKill) {
		super();
		this.previousKill = previousKill;
		this.nextKill = nextKill;
	}

	public Kill getPreviousKill() {
		return previousKill;
	}

	public void setPreviousKill(Kill previousKill) {
		this.previousKill = previousKill;
	}

	public Kill getNextKill() {
		return nextKill;
	}

	public void setNextKill(Kill nextKill) {
		this.nextKill = nextKill;
	}

	@Override
	public String toString() {
		return "KillPair [previousKill=" + previousKill + ", nextKill=" + nextKill + "]";
	}
	
	
	
}

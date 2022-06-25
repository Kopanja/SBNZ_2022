package com.valorant.clip.editor.valorantclip.model;

import org.kie.api.definition.type.Position;
import org.kie.api.definition.type.PropertyReactive;

public class Kill {

	private String killer;
	private String defeated;
	private boolean hasFrames;
	private boolean isKillAlly;
	private boolean isDefeatAlly;
	private double time;

	
	public Kill() {
		super();
	}

	
	public Kill(double time) {
		super();
		this.time = time;
	}
	
	

	public Kill(String killer, String defeated, double time) {
		super();
		this.killer = killer;
		this.defeated = defeated;
		this.time = time;
	}

	

	public Kill(String killer, String defeated, boolean hasFrames, boolean isKillAlly, boolean isDefeatAlly,
			double time) {
		super();
		this.killer = killer;
		this.defeated = defeated;
		this.hasFrames = hasFrames;
		this.isKillAlly = isKillAlly;
		this.isDefeatAlly = isDefeatAlly;
		this.time = time;
	}


	public double getTime() {
		return time;
	}

	public void setTime(double time) {
		this.time = time;
	}


	public String getKiller() {
		return killer;
	}


	public void setKiller(String killer) {
		this.killer = killer;
	}


	public String getDefeated() {
		return defeated;
	}


	public void setDefeated(String defeated) {
		this.defeated = defeated;
	}

	

	public boolean isHasFrames() {
		return hasFrames;
	}


	public void setHasFrames(boolean hasFrames) {
		this.hasFrames = hasFrames;
	}

	

	public boolean getIsKillAlly() {
        return isKillAlly;
    }

	public void setKillAlly(boolean isKillAlly) {
		this.isKillAlly = isKillAlly;
	}


	public boolean getIsDefeatAlly() {
		return isDefeatAlly;
	}


	public void setDefeatAlly(boolean isDefeatAlly) {
		this.isDefeatAlly = isDefeatAlly;
	}

	

	@Override
	public String toString() {
		
		
		return "Kill [killer=" + killer + ", defeated=" + defeated + ", hasFrames=" + hasFrames + ", isKillAlly="
		+ isKillAlly + ", isDefeatAlly=" + isDefeatAlly + ", time=" + time + "]";
		
	}


	
	
	
	
}

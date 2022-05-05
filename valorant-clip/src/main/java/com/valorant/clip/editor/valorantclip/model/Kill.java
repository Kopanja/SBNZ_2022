package com.valorant.clip.editor.valorantclip.model;

public class Kill {

	private String killer;
	private String defeated;
	private boolean hasFrames;
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


	@Override
	public String toString() {
		return "Kill [killer=" + killer + ", defeated=" + defeated + ", time=" + time + "]";
	}
	
	
	
}

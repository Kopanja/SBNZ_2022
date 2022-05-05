package com.valorant.clip.editor.valorantclip.model;

public class QuadraKill extends ClipEvent {

	public QuadraKill() {

	}

	public QuadraKill(double startTime, double endTime) {
		
		super(startTime, endTime);
		this.setTitle("Quadra Kill");
	}

	
	
	@Override
	public String toString() {
		return "QuadraKill [getStartTime()=" + getStartTime() + ", getEndTime()=" + getEndTime() + ", getClass()="
				+ getClass() + ", hashCode()=" + hashCode() + ", toString()=" + super.toString() + "]";
	}
	
		
	

}

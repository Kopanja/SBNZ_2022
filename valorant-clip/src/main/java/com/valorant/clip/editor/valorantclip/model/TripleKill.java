package com.valorant.clip.editor.valorantclip.model;

public class TripleKill extends ClipEvent {

	
	public TripleKill() {
		
	}
	
	public TripleKill(double startTime, double endTime) {
		super(startTime,endTime);
		this.setTitle("Triple Kill");
	}
	@Override
	public String toString() {
		return "TripleKill [getStartTime()=" + getStartTime() + ", getEndTime()=" + getEndTime() + ", getClass()="
				+ getClass() + ", hashCode()=" + hashCode() + ", toString()=" + super.toString() + "]";
	}

	
	
	
}

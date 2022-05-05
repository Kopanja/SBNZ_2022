package com.valorant.clip.editor.valorantclip.model;

public class Ace extends ClipEvent {

	public Ace() {

	}

	public Ace(double startTime, double endTime) {
		super(startTime, endTime);
		this.setTitle("Ace");
	}
	@Override
	public String toString() {
		return "Ace [getStartTime()=" + getStartTime() + ", getEndTime()=" + getEndTime() + ", getClass()=" + getClass()
				+ ", hashCode()=" + hashCode() + ", toString()=" + super.toString() + "]";
	}

	
}

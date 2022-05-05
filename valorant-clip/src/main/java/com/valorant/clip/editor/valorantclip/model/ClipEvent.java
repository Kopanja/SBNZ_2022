package com.valorant.clip.editor.valorantclip.model;

public class ClipEvent {
	
	private double startTime;
	private double endTime;
	private String title;
	
	
	public ClipEvent() {
		super();
	}
	public ClipEvent(double startTime, double endTime) {
		super();
		this.startTime = startTime;
		this.endTime = endTime;
	}
	public double getStartTime() {
		return startTime;
	}
	public void setStartTime(double startTime) {
		this.startTime = startTime;
	}
	public double getEndTime() {
		return endTime;
	}
	public void setEndTime(double endTime) {
		this.endTime = endTime;
	}
	
	public void createTitle() {
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	
	

}

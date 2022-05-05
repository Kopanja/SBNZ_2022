package com.valorant.clip.editor.valorantclip.model;

import java.util.List;

public class FrameAgentDetectionEvent {

	private double time;
	private List<BoundingBox> bboxes;
	
	
	
	public FrameAgentDetectionEvent() {
		super();
	}



	public FrameAgentDetectionEvent(double time, List<BoundingBox> bboxes) {
		super();
		this.time = time;
		this.bboxes = bboxes;
	}



	public double getTime() {
		return time;
	}



	public void setTime(double time) {
		this.time = time;
	}



	public List<BoundingBox> getBboxes() {
		return bboxes;
	}



	public void setBboxes(List<BoundingBox> bboxes) {
		this.bboxes = bboxes;
	}



	@Override
	public String toString() {
		return "FrameAgentDetectionEvent [time=" + time + ", bboxes=" + bboxes + "]";
	}
	
	
	
}

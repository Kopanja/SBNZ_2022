package com.valorant.clip.editor.valorantclip.model;

public class AgentDetectedEvent {

	private int x_top;
	private int x_bot;
	private int y_top;
	private int y_bot;
	private double time;
	
	
	
	public AgentDetectedEvent() {
		super();
	}



	public AgentDetectedEvent(int x_top, int x_bot, int y_top, int y_bot, double time) {
		super();
		this.x_top = x_top;
		this.x_bot = x_bot;
		this.y_top = y_top;
		this.y_bot = y_bot;
		this.time = time;
	}



	public int getX_top() {
		return x_top;
	}



	public void setX_top(int x_top) {
		this.x_top = x_top;
	}



	public int getX_bot() {
		return x_bot;
	}



	public void setX_bot(int x_bot) {
		this.x_bot = x_bot;
	}



	public int getY_top() {
		return y_top;
	}



	public void setY_top(int y_top) {
		this.y_top = y_top;
	}



	public int getY_bot() {
		return y_bot;
	}



	public void setY_bot(int y_bot) {
		this.y_bot = y_bot;
	}



	public double getTime() {
		return time;
	}



	public void setTime(double time) {
		this.time = time;
	}



	@Override
	public String toString() {
		return "AgentDetectedEvent [x_top=" + x_top + ", x_bot=" + x_bot + ", y_top=" + y_top + ", y_bot=" + y_bot
				+ ", time=" + time + "]";
	}
	
	
}

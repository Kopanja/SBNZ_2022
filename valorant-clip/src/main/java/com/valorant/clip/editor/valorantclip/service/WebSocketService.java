package com.valorant.clip.editor.valorantclip.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

import com.valorant.clip.editor.valorantclip.model.ClipEvent;

@Service
public class WebSocketService {
	// @Autowired
	private static SimpMessagingTemplate template;

	@Autowired
	public WebSocketService(SimpMessagingTemplate template) {
		this.template = template;

	}

	public static void send(ClipEvent clipEvent) {
		template.convertAndSend("/topic", clipEvent);
	}
}

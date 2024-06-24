---
Please provide me with more information about the mission you want to describe! I need some context to help you create a compelling and effective mission statement. 

For example, tell me: "* **What is the mission about?** (e.g., a business, a non-profit organization, a personal goal)"
* **What are the goals of the mission?** (e.g., to improve the environment, to create a new product, to inspire people)
* **What are the values that guide the mission?** (e.g., innovation, sustainability, social responsibility)
* **Who is the target audience?** (e.g., customers, employees, the general public)

Once I have this information, I can help you craft a powerful mission statement that clearly outlines your purpose and inspires action.
---

[

Introduction
------------

](/docs/api-reference/introduction)

You can interact with the API through HTTP requests from any language, via our official Python bindings, our official Node.js library, or a [community-maintained library](/docs/libraries/community-libraries).

To install the official Python bindings, run the following command:

    pip install openai

To install the official Node.js library, run the following command in your Node.js project directory:

    npm install openai@^4.0.0

[

Authentication
--------------

](/docs/api-reference/authentication)

[

### API keys

](/docs/api-reference/api-keys)

The OpenAI API uses API keys for authentication. You can create API keys at a user or service account level. Service accounts are tied to a "bot" individual and should be used to provision access for production systems. Each API key can be scoped to one of the following,

1.  **Project keys** - Provides access to a single project (**preferred option**); access [Project API keys](/settings/organization/general) by selecting the specific project you wish to generate keys against.
2.  **User keys** - Our legacy keys. Provides access to all organizations and all projects that user has been added to; access [API Keys](/account/api-keys) to view your available keys. We highly advise transitioning to project keys for best security practices, although access via this method is currently still supported.

**Remember that your API key is a secret!** Do not share it with others or expose it in any client-side code (browsers, apps). Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an `Authorization` HTTP header as follows:

    Authorization: Bearer OPENAI_API_KEY

[

### Organizations and projects (optional)

](/docs/api-reference/organizations-and-projects-optional)

For users who belong to multiple organizations or are accessing their projects through their legacy user API key, you can pass a header to specify which organization and project is used for an API request. Usage from these API requests will count as usage for the specified organization and project.

To access the `Default project` in an organization, leave out the `OpenAI-Project` header

Example curl command:

    1
    2
    3
    4
    curl https://api.openai.com/v1/models \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Organization: YOUR_ORG_ID" \
      -H "OpenAI-Project: $PROJECT_ID"

Example with the `openai` Python package:

    1
    2
    3
    4
    5
    6
    from openai import OpenAI
    
    client = OpenAI(
      organization='YOUR_ORG_ID',
      project='$PROJECT_ID',
    )

Example with the `openai` Node.js package:

    1
    2
    3
    4
    5
    6
    import OpenAI from "openai";
    
    const openai = new OpenAI({
        organization: "YOUR_ORG_ID",
        project: "$PROJECT_ID",
    });

Organization IDs can be found on your [Organization settings](/account/organization) page. Project IDs can be found on your [General settings](/settings) page by selecting the specific project.

[

Making requests
---------------

](/docs/api-reference/making-requests)

You can paste the command below into your terminal to run your first API request. Make sure to replace `$OPENAI_API_KEY` with your secret API key. If you are using a legacy user key and you have multiple projects, you will also need to [specify the Project Id](/docs/api-reference/authentication). For improved security, we recommend transitioning to project based keys instead.

    1
    2
    3
    4
    5
    6
    7
    8
    curl https://api.openai.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
         "model": "gpt-3.5-turbo",
         "messages": [{"role": "user", "content": "Say this is a test!"}],
         "temperature": 0.7
       }'

This request queries the `gpt-3.5-turbo` model (which under the hood points to a [`gpt-3.5-turbo` model variant](/docs/models/gpt-3-5-turbo)) to complete the text starting with a prompt of "_Say this is a test_". You should get a response back that resembles the following:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    {
        "id": "chatcmpl-abc123",
        "object": "chat.completion",
        "created": 1677858242,
        "model": "gpt-3.5-turbo-0613",
        "usage": {
            "prompt_tokens": 13,
            "completion_tokens": 7,
            "total_tokens": 20
        },
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "\n\nThis is a test!"
                },
                "logprobs": null,
                "finish_reason": "stop",
                "index": 0
            }
        ]
    }

Now that you've generated your first chat completion, let's break down the [response object](/docs/api-reference/chat/object). We can see the `finish_reason` is `stop` which means the API returned the full chat completion generated by the model without running into any limits. In the choices list, we only generated a single message but you can set the `n` parameter to generate multiple messages choices.

[

Streaming
---------

](/docs/api-reference/streaming)

The OpenAI API provides the ability to stream responses back to a client in order to allow partial results for certain requests. To achieve this, we follow the [Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) standard. Our official [Node](https://github.com/openai/openai-node?tab=readme-ov-file#streaming-responses) and [Python](https://github.com/openai/openai-python?tab=readme-ov-file#streaming-responses) libraries include helpers to make parsing these events simpler.

Streaming is supported for both the [Chat Completions API](/docs/api-reference/chat/streaming) and the [Assistants API](/docs/api-reference/runs/createRun). This section focuses on how streaming works for Chat Completions. Learn more about how streaming works in the Assistants API [here](/docs/assistants/overview/step-4-create-a-run).

In Python, a streaming request looks like:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    from openai import OpenAI
    
    client = OpenAI()
    
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

In Node / Typescript, a streaming request looks like:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    import OpenAI from "openai";
    
    const openai = new OpenAI();
    
    async function main() {
        const stream = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: "Say this is a test" }],
            stream: true,
        });
        for await (const chunk of stream) {
            process.stdout.write(chunk.choices[0]?.delta?.content || "");
        }
    }
    
    main();

[

#### Parsing Server-sent events

](/docs/api-reference/parsing-server-sent-events)

Parsing Server-sent events is non-trivial and should be done with caution. Simple strategies like splitting by a new line may result in parsing errors. We recommend using [existing client libraries](/docs/libraries) when possible.

[

Audio
-----

](/docs/api-reference/audio)

Learn how to turn audio into text or text into audio.

Related guide: [Speech to text](/docs/guides/speech-to-text)

[

Create speech
-------------

](/docs/api-reference/audio/createSpeech)

post https://api.openai.com/v1/audio/speech

Generates audio from the input text.

### Request body

[](#audio-createspeech-model)

model

string

Required

One of the available [TTS models](/docs/models/tts): `tts-1` or `tts-1-hd`

[](#audio-createspeech-input)

input

string

Required

The text to generate audio for. The maximum length is 4096 characters.

[](#audio-createspeech-voice)

voice

string

Required

The voice to use when generating the audio. Supported voices are `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech/voice-options).

[](#audio-createspeech-response_format)

response\_format

string

Optional

Defaults to mp3

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

[](#audio-createspeech-speed)

speed

number

Optional

Defaults to 1

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

### Returns

The audio file content.

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    4
    5
    6
    7
    8
    9
    curl https://api.openai.com/v1/audio/speech \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "tts-1",
        "input": "The quick brown fox jumped over the lazy dog.",
        "voice": "alloy"
      }' \
      --output speech.mp3

[

Create transcription
--------------------

](/docs/api-reference/audio/createTranscription)

post https://api.openai.com/v1/audio/transcriptions

Transcribes audio into the input language.

### Request body

[](#audio-createtranscription-file)

file

file

Required

The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[](#audio-createtranscription-model)

model

string

Required

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

[](#audio-createtranscription-language)

language

string

Optional

The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

[](#audio-createtranscription-prompt)

prompt

string

Optional

An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.

[](#audio-createtranscription-response_format)

response\_format

string

Optional

Defaults to json

The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

[](#audio-createtranscription-temperature)

temperature

number

Optional

Defaults to 0

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

[](#audio-createtranscription-timestamp_granularities)

timestamp\_granularities\[\]

array

Optional

Defaults to segment

The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.

### Returns

The [transcription object](/docs/api-reference/audio/json-object) or a [verbose transcription object](/docs/api-reference/audio/verbose-json-object).

Default‍Word timestamps‍Segment timestamps‍

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/audio/transcriptions \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: multipart/form-data" \
      -F file="@/path/to/file/audio.mp3" \
      -F model="whisper-1"

Response

    1
    2
    3
    {
      "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
    }

[

Create translation
------------------

](/docs/api-reference/audio/createTranslation)

post https://api.openai.com/v1/audio/translations

Translates audio into English.

### Request body

[](#audio-createtranslation-file)

file

file

Required

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[](#audio-createtranslation-model)

model

string

Required

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

[](#audio-createtranslation-prompt)

prompt

string

Optional

An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.

[](#audio-createtranslation-response_format)

response\_format

string

Optional

Defaults to json

The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

[](#audio-createtranslation-temperature)

temperature

number

Optional

Defaults to 0

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

### Returns

The translated text.

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/audio/translations \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: multipart/form-data" \
      -F file="@/path/to/file/german.m4a" \
      -F model="whisper-1"

Response

    1
    2
    3
    {
      "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
    }

[

The transcription object (JSON)
-------------------------------

](/docs/api-reference/audio/json-object)

Represents a transcription response returned by model, based on the provided input.

[](#audio/json-object-text)

text

string

The transcribed text.

The transcription object (JSON)

    1
    2
    3
    {
      "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
    }

[

The transcription object (Verbose JSON)
---------------------------------------

](/docs/api-reference/audio/verbose-json-object)

Represents a verbose json transcription response returned by model, based on the provided input.

[](#audio/verbose-json-object-language)

language

string

The language of the input audio.

[](#audio/verbose-json-object-duration)

duration

string

The duration of the input audio.

[](#audio/verbose-json-object-text)

text

string

The transcribed text.

[](#audio/verbose-json-object-words)

words

array

Extracted words and their corresponding timestamps.

Show properties

[](#audio/verbose-json-object-segments)

segments

array

Segments of the transcribed text and their corresponding details.

Show properties

The transcription object (Verbose JSON)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    {
      "task": "transcribe",
      "language": "english",
      "duration": 8.470000267028809,
      "text": "The beach was a popular spot on a hot summer day. People were swimming in the ocean, building sandcastles, and playing beach volleyball.",
      "segments": [
        {
          "id": 0,
          "seek": 0,
          "start": 0.0,
          "end": 3.319999933242798,
          "text": " The beach was a popular spot on a hot summer day.",
          "tokens": [
            50364, 440, 7534, 390, 257, 3743, 4008, 322, 257, 2368, 4266, 786, 13, 50530
          ],
          "temperature": 0.0,
          "avg_logprob": -0.2860786020755768,
          "compression_ratio": 1.2363636493682861,
          "no_speech_prob": 0.00985979475080967
        },
        ...
      ]
    }

[

Chat
----

](/docs/api-reference/chat)

Given a list of messages comprising a conversation, the model will return a response.

Related guide: [Chat Completions](/docs/guides/text-generation)

[

Create chat completion
----------------------

](/docs/api-reference/chat/create)

post https://api.openai.com/v1/chat/completions

Creates a model response for the given chat conversation.

### Request body

[](#chat-create-messages)

messages

array

Required

A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).

Show possible types

[](#chat-create-model)

model

string

Required

ID of the model to use. See the [model endpoint compatibility](/docs/models/model-endpoint-compatibility) table for details on which models work with the Chat API.

[](#chat-create-frequency_penalty)

frequency\_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)

[](#chat-create-logit_bias)

logit\_bias

map

Optional

Defaults to null

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

[](#chat-create-logprobs)

logprobs

boolean or null

Optional

Defaults to false

Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.

[](#chat-create-top_logprobs)

top\_logprobs

integer or null

Optional

An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.

[](#chat-create-max_tokens)

max\_tokens

integer or null

Optional

The maximum number of [tokens](/tokenizer) that can be generated in the chat completion.

The total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

[](#chat-create-n)

n

integer or null

Optional

Defaults to 1

How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

[](#chat-create-presence_penalty)

presence\_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)

[](#chat-create-response_format)

response\_format

object

Optional

An object specifying the format that the model must output. Compatible with [GPT-4 Turbo](/docs/models/gpt-4-and-gpt-4-turbo) and all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show properties

[](#chat-create-seed)

seed

integer or null

Optional

This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

[](#chat-create-stop)

stop

string / array / null

Optional

Defaults to null

Up to 4 sequences where the API will stop generating further tokens.

[](#chat-create-stream)

stream

boolean or null

Optional

Defaults to false

If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

[](#chat-create-stream_options)

stream\_options

object or null

Optional

Defaults to null

Options for streaming response. Only set this when you set `stream: true`.

Show properties

[](#chat-create-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or `top_p` but not both.

[](#chat-create-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or `temperature` but not both.

[](#chat-create-tools)

tools

array

Optional

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

Show properties

[](#chat-create-tool_choice)

tool\_choice

string or object

Optional

Controls which (if any) tool is called by the model. `none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

Show possible types

[](#chat-create-parallel_tool_calls)

parallel\_tool\_calls

boolean

Optional

Defaults to true

Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.

[](#chat-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

[](#chat-create-function_call)

function\_call

Deprecated

string or object

Optional

Deprecated in favor of `tool_choice`.

Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

`none` is the default when no functions are present. `auto` is the default if functions are present.

Show possible types

[](#chat-create-functions)

functions

Deprecated

array

Optional

Deprecated in favor of `tools`.

A list of functions the model may generate JSON inputs for.

Show properties

### Returns

Returns a [chat completion](/docs/api-reference/chat/object) object, or a streamed sequence of [chat completion chunk](/docs/api-reference/chat/streaming) objects if the request is streamed.

Default‍Image input‍Streaming‍Functions‍Logprobs‍

Example request

gpt-4o

gpt-4ogpt-3.5-turbo

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    curl https://api.openai.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "gpt-4o",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant."
          },
          {
            "role": "user",
            "content": "Hello!"
          }
        ]
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    {
      "id": "chatcmpl-123",
      "object": "chat.completion",
      "created": 1677652288,
      "model": "gpt-3.5-turbo-0125",
      "system_fingerprint": "fp_44709d6fcb",
      "choices": [{
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "\n\nHello there, how may I assist you today?",
        },
        "logprobs": null,
        "finish_reason": "stop"
      }],
      "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
      }
    }

[

The chat completion object
--------------------------

](/docs/api-reference/chat/object)

Represents a chat completion response returned by model, based on the provided input.

[](#chat/object-id)

id

string

A unique identifier for the chat completion.

[](#chat/object-choices)

choices

array

A list of chat completion choices. Can be more than one if `n` is greater than 1.

Show properties

[](#chat/object-created)

created

integer

The Unix timestamp (in seconds) of when the chat completion was created.

[](#chat/object-model)

model

string

The model used for the chat completion.

[](#chat/object-system_fingerprint)

system\_fingerprint

string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](#chat/object-object)

object

string

The object type, which is always `chat.completion`.

[](#chat/object-usage)

usage

object

Usage statistics for the completion request.

Show properties

The chat completion object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    {
      "id": "chatcmpl-123",
      "object": "chat.completion",
      "created": 1677652288,
      "model": "gpt-3.5-turbo-0125",
      "system_fingerprint": "fp_44709d6fcb",
      "choices": [{
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "\n\nHello there, how may I assist you today?",
        },
        "logprobs": null,
        "finish_reason": "stop"
      }],
      "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
      }
    }

[

The chat completion chunk object
--------------------------------

](/docs/api-reference/chat/streaming)

Represents a streamed chunk of a chat completion response returned by model, based on the provided input.

[](#chat/streaming-id)

id

string

A unique identifier for the chat completion. Each chunk has the same ID.

[](#chat/streaming-choices)

choices

array

A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the last chunk if you set `stream_options: {"include_usage": true}`.

Show properties

[](#chat/streaming-created)

created

integer

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

[](#chat/streaming-model)

model

string

The model to generate the completion.

[](#chat/streaming-system_fingerprint)

system\_fingerprint

string

This fingerprint represents the backend configuration that the model runs with. Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](#chat/streaming-object)

object

string

The object type, which is always `chat.completion.chunk`.

[](#chat/streaming-usage)

usage

object

An optional field that will only be present when you set `stream_options: {"include_usage": true}` in your request. When present, it contains a null value except for the last chunk which contains the token usage statistics for the entire request.

Show properties

The chat completion chunk object

    1
    2
    3
    4
    5
    6
    7
    {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}
    
    {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}
    
    ....
    
    {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}]}

[

Embeddings
----------

](/docs/api-reference/embeddings)

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

Related guide: [Embeddings](/docs/guides/embeddings)

[

Create embeddings
-----------------

](/docs/api-reference/embeddings/create)

post https://api.openai.com/v1/embeddings

Creates an embedding vector representing the input text.

### Request body

[](#embeddings-create-input)

input

string or array

Required

Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8192 tokens for `text-embedding-ada-002`), cannot be an empty string, and any array must be 2048 dimensions or less. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

Show possible types

[](#embeddings-create-model)

model

string

Required

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

[](#embeddings-create-encoding_format)

encoding\_format

string

Optional

Defaults to float

The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).

[](#embeddings-create-dimensions)

dimensions

integer

Optional

The number of dimensions the resulting output embeddings should have. Only supported in `text-embedding-3` and later models.

[](#embeddings-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

### Returns

A list of [embedding](/docs/api-reference/embeddings/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    curl https://api.openai.com/v1/embeddings \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "input": "The food was delicious and the waiter...",
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "object": "list",
      "data": [
        {
          "object": "embedding",
          "embedding": [
            0.0023064255,
            -0.009327292,
            .... (1536 floats total for ada-002)
            -0.0028842222,
          ],
          "index": 0
        }
      ],
      "model": "text-embedding-ada-002",
      "usage": {
        "prompt_tokens": 8,
        "total_tokens": 8
      }
    }

[

The embedding object
--------------------

](/docs/api-reference/embeddings/object)

Represents an embedding vector returned by embedding endpoint.

[](#embeddings/object-index)

index

integer

The index of the embedding in the list of embeddings.

[](#embeddings/object-embedding)

embedding

array

The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the [embedding guide](/docs/guides/embeddings).

[](#embeddings/object-object)

object

string

The object type, which is always "embedding".

The embedding object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    {
      "object": "embedding",
      "embedding": [
        0.0023064255,
        -0.009327292,
        .... (1536 floats total for ada-002)
        -0.0028842222,
      ],
      "index": 0
    }

[

Fine-tuning
-----------

](/docs/api-reference/fine-tuning)

Manage fine-tuning jobs to tailor a model to your specific training data.

Related guide: [Fine-tune models](/docs/guides/fine-tuning)

[

Create fine-tuning job
----------------------

](/docs/api-reference/fine-tuning/create)

post https://api.openai.com/v1/fine\_tuning/jobs

Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/fine-tuning)

### Request body

[](#fine-tuning-create-model)

model

string

Required

The name of the model to fine-tune. You can select one of the [supported models](/docs/guides/fine-tuning/what-models-can-be-fine-tuned).

[](#fine-tuning-create-training_file)

training\_file

string

Required

The ID of an uploaded file that contains training data.

See [upload file](/docs/api-reference/files/create) for how to upload a file.

Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

The contents of the file should differ depending on if the model uses the [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) format.

See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

[](#fine-tuning-create-hyperparameters)

hyperparameters

object

Optional

The hyperparameters used for the fine-tuning job.

Show properties

[](#fine-tuning-create-suffix)

suffix

string or null

Optional

Defaults to null

A string of up to 18 characters that will be added to your fine-tuned model name.

For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.

[](#fine-tuning-create-validation_file)

validation\_file

string or null

Optional

The ID of an uploaded file that contains validation data.

If you provide this file, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in the fine-tuning results file. The same data should not be present in both train and validation files.

Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

[](#fine-tuning-create-integrations)

integrations

array or null

Optional

A list of integrations to enable for your fine-tuning job.

Show properties

[](#fine-tuning-create-seed)

seed

integer or null

Optional

The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed is not specified, one will be generated for you.

### Returns

A [fine-tuning.job](/docs/api-reference/fine-tuning/object) object.

Default‍Epochs‍Validation file‍W&B Integration‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/fine_tuning/jobs \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "training_file": "file-BK7bzQj3FfZFXr7DbL6xJwfo",
        "model": "gpt-3.5-turbo"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    {
      "object": "fine_tuning.job",
      "id": "ftjob-abc123",
      "model": "gpt-3.5-turbo-0125",
      "created_at": 1614807352,
      "fine_tuned_model": null,
      "organization_id": "org-123",
      "result_files": [],
      "status": "queued",
      "validation_file": null,
      "training_file": "file-abc123",
    }

[

List fine-tuning jobs
---------------------

](/docs/api-reference/fine-tuning/list)

get https://api.openai.com/v1/fine\_tuning/jobs

List your organization's fine-tuning jobs

### Query parameters

[](#fine-tuning-list-after)

after

string

Optional

Identifier for the last job from the previous pagination request.

[](#fine-tuning-list-limit)

limit

integer

Optional

Defaults to 20

Number of fine-tuning jobs to retrieve.

### Returns

A list of paginated [fine-tuning job](/docs/api-reference/fine-tuning/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/fine_tuning/jobs?limit=2 \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    {
      "object": "list",
      "data": [
        {
          "object": "fine_tuning.job.event",
          "id": "ft-event-TjX0lMfOniCZX64t9PUQT5hn",
          "created_at": 1689813489,
          "level": "warn",
          "message": "Fine tuning process stopping due to job cancellation",
          "data": null,
          "type": "message"
        },
        { ... },
        { ... }
      ], "has_more": true
    }

[

List fine-tuning events
-----------------------

](/docs/api-reference/fine-tuning/list-events)

get https://api.openai.com/v1/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

Get status updates for a fine-tuning job.

### Path parameters

[](#fine-tuning-list-events-fine_tuning_job_id)

fine\_tuning\_job\_id

string

Required

The ID of the fine-tuning job to get events for.

### Query parameters

[](#fine-tuning-list-events-after)

after

string

Optional

Identifier for the last event from the previous pagination request.

[](#fine-tuning-list-events-limit)

limit

integer

Optional

Defaults to 20

Number of events to retrieve.

### Returns

A list of fine-tuning event objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/events \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    {
      "object": "list",
      "data": [
        {
          "object": "fine_tuning.job.event",
          "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
          "created_at": 1692407401,
          "level": "info",
          "message": "Fine tuning job successfully completed",
          "data": null,
          "type": "message"
        },
        {
          "object": "fine_tuning.job.event",
          "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
          "created_at": 1692407400,
          "level": "info",
          "message": "New fine-tuned model created: ft:gpt-3.5-turbo:openai::7p4lURel",
          "data": null,
          "type": "message"
        }
      ],
      "has_more": true
    }

[

List fine-tuning checkpoints
----------------------------

](/docs/api-reference/fine-tuning/list-checkpoints)

get https://api.openai.com/v1/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

List checkpoints for a fine-tuning job.

### Path parameters

[](#fine-tuning-list-checkpoints-fine_tuning_job_id)

fine\_tuning\_job\_id

string

Required

The ID of the fine-tuning job to get checkpoints for.

### Query parameters

[](#fine-tuning-list-checkpoints-after)

after

string

Optional

Identifier for the last checkpoint ID from the previous pagination request.

[](#fine-tuning-list-checkpoints-limit)

limit

integer

Optional

Defaults to 10

Number of checkpoints to retrieve.

### Returns

A list of fine-tuning [checkpoint objects](/docs/api-reference/fine-tuning/checkpoint-object) for a fine-tuning job.

Example request

curl

Select librarycurl

    1
    2
    curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/checkpoints \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    {
      "object": "list"
      "data": [
        {
          "object": "fine_tuning.job.checkpoint",
          "id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
          "created_at": 1519129973,
          "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom-suffix:96olL566:ckpt-step-2000",
          "metrics": {
            "full_valid_loss": 0.134,
            "full_valid_mean_token_accuracy": 0.874
          },
          "fine_tuning_job_id": "ftjob-abc123",
          "step_number": 2000,
        },
        {
          "object": "fine_tuning.job.checkpoint",
          "id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
          "created_at": 1519129833,
          "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
          "metrics": {
            "full_valid_loss": 0.167,
            "full_valid_mean_token_accuracy": 0.781
          },
          "fine_tuning_job_id": "ftjob-abc123",
          "step_number": 1000,
        },
      ],
      "first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
      "last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
      "has_more": true
    }

[

Retrieve fine-tuning job
------------------------

](/docs/api-reference/fine-tuning/retrieve)

get https://api.openai.com/v1/fine\_tuning/jobs/{fine\_tuning\_job\_id}

Get info about a fine-tuning job.

[Learn more about fine-tuning](/docs/guides/fine-tuning)

### Path parameters

[](#fine-tuning-retrieve-fine_tuning_job_id)

fine\_tuning\_job\_id

string

Required

The ID of the fine-tuning job.

### Returns

The [fine-tuning](/docs/api-reference/fine-tuning/object) object with the given ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    {
      "object": "fine_tuning.job",
      "id": "ftjob-abc123",
      "model": "davinci-002",
      "created_at": 1692661014,
      "finished_at": 1692661190,
      "fine_tuned_model": "ft:davinci-002:my-org:custom_suffix:7q8mpxmy",
      "organization_id": "org-123",
      "result_files": [
          "file-abc123"
      ],
      "status": "succeeded",
      "validation_file": null,
      "training_file": "file-abc123",
      "hyperparameters": {
          "n_epochs": 4,
          "batch_size": 1,
          "learning_rate_multiplier": 1.0
      },
      "trained_tokens": 5768,
      "integrations": [],
      "seed": 0,
      "estimated_finish": 0
    }

[

Cancel fine-tuning
------------------

](/docs/api-reference/fine-tuning/cancel)

post https://api.openai.com/v1/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

Immediately cancel a fine-tune job.

### Path parameters

[](#fine-tuning-cancel-fine_tuning_job_id)

fine\_tuning\_job\_id

string

Required

The ID of the fine-tuning job to cancel.

### Returns

The cancelled [fine-tuning](/docs/api-reference/fine-tuning/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl -X POST https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/cancel \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    {
      "object": "fine_tuning.job",
      "id": "ftjob-abc123",
      "model": "gpt-3.5-turbo-0125",
      "created_at": 1689376978,
      "fine_tuned_model": null,
      "organization_id": "org-123",
      "result_files": [],
      "hyperparameters": {
        "n_epochs":  "auto"
      },
      "status": "cancelled",
      "validation_file": "file-abc123",
      "training_file": "file-abc123"
    }

[

Training format for chat models
-------------------------------

](/docs/api-reference/fine-tuning/chat-input)

The per-line training example of a fine-tuning input file for chat models

[](#fine-tuning/chat-input-messages)

messages

array

Show possible types

[](#fine-tuning/chat-input-functions)

functions

array

A list of functions the model may generate JSON inputs for.

Show properties

Training format for chat models

    {"messages":[{"role":"user","content":"What is the weather in San Francisco?"},{"role":"assistant","function_call":{"name":"get_current_weather","arguments":"{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"}}],"functions":[{"name":"get_current_weather","description":"Get the current weather","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and country, eg. San Francisco, USA"},"format":{"type":"string","enum":["celsius","fahrenheit"]}},"required":["location","format"]}}]}

[

Training format for completions models
--------------------------------------

](/docs/api-reference/fine-tuning/completions-input)

The per-line training example of a fine-tuning input file for completions models

[](#fine-tuning/completions-input-prompt)

prompt

string

The input prompt for this training example.

[](#fine-tuning/completions-input-completion)

completion

string

The desired completion for this training example.

Training format for completions models

    {"prompt": "What is the answer to 2+2", "completion": "4"}

[

The fine-tuning job object
--------------------------

](/docs/api-reference/fine-tuning/object)

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

[](#fine-tuning/object-id)

id

string

The object identifier, which can be referenced in the API endpoints.

[](#fine-tuning/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the fine-tuning job was created.

[](#fine-tuning/object-error)

error

object or null

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

Show properties

[](#fine-tuning/object-fine_tuned_model)

fine\_tuned\_model

string or null

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

[](#fine-tuning/object-finished_at)

finished\_at

integer or null

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

[](#fine-tuning/object-hyperparameters)

hyperparameters

object

The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

Show properties

[](#fine-tuning/object-model)

model

string

The base model that is being fine-tuned.

[](#fine-tuning/object-object)

object

string

The object type, which is always "fine\_tuning.job".

[](#fine-tuning/object-organization_id)

organization\_id

string

The organization that owns the fine-tuning job.

[](#fine-tuning/object-result_files)

result\_files

array

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents).

[](#fine-tuning/object-status)

status

string

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

[](#fine-tuning/object-trained_tokens)

trained\_tokens

integer or null

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

[](#fine-tuning/object-training_file)

training\_file

string

The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents).

[](#fine-tuning/object-validation_file)

validation\_file

string or null

The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents).

[](#fine-tuning/object-integrations)

integrations

array or null

A list of integrations to enable for this fine-tuning job.

Show possible types

[](#fine-tuning/object-seed)

seed

integer

The seed used for the fine-tuning job.

[](#fine-tuning/object-estimated_finish)

estimated\_finish

integer or null

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

The fine-tuning job object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    {
      "object": "fine_tuning.job",
      "id": "ftjob-abc123",
      "model": "davinci-002",
      "created_at": 1692661014,
      "finished_at": 1692661190,
      "fine_tuned_model": "ft:davinci-002:my-org:custom_suffix:7q8mpxmy",
      "organization_id": "org-123",
      "result_files": [
          "file-abc123"
      ],
      "status": "succeeded",
      "validation_file": null,
      "training_file": "file-abc123",
      "hyperparameters": {
          "n_epochs": 4,
          "batch_size": 1,
          "learning_rate_multiplier": 1.0
      },
      "trained_tokens": 5768,
      "integrations": [],
      "seed": 0,
      "estimated_finish": 0
    }

[

The fine-tuning job event object
--------------------------------

](/docs/api-reference/fine-tuning/event-object)

Fine-tuning job event object

[](#fine-tuning/event-object-id)

id

string

[](#fine-tuning/event-object-created_at)

created\_at

integer

[](#fine-tuning/event-object-level)

level

string

[](#fine-tuning/event-object-message)

message

string

[](#fine-tuning/event-object-object)

object

string

The fine-tuning job event object

    1
    2
    3
    4
    5
    6
    7
    {
      "object": "fine_tuning.job.event",
      "id": "ftevent-abc123"
      "created_at": 1677610602,
      "level": "info",
      "message": "Created fine-tuning job"
    }

[

The fine-tuning job checkpoint object
-------------------------------------

](/docs/api-reference/fine-tuning/checkpoint-object)

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

[](#fine-tuning/checkpoint-object-id)

id

string

The checkpoint identifier, which can be referenced in the API endpoints.

[](#fine-tuning/checkpoint-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the checkpoint was created.

[](#fine-tuning/checkpoint-object-fine_tuned_model_checkpoint)

fine\_tuned\_model\_checkpoint

string

The name of the fine-tuned checkpoint model that is created.

[](#fine-tuning/checkpoint-object-step_number)

step\_number

integer

The step number that the checkpoint was created at.

[](#fine-tuning/checkpoint-object-metrics)

metrics

object

Metrics at the step number during the fine-tuning job.

Show properties

[](#fine-tuning/checkpoint-object-fine_tuning_job_id)

fine\_tuning\_job\_id

string

The name of the fine-tuning job that this checkpoint was created from.

[](#fine-tuning/checkpoint-object-object)

object

string

The object type, which is always "fine\_tuning.job.checkpoint".

The fine-tuning job checkpoint object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    {
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_qtZ5Gyk4BLq1SfLFWp3RtO3P",
      "created_at": 1712211699,
      "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom_suffix:9ABel2dg:ckpt-step-88",
      "fine_tuning_job_id": "ftjob-fpbNQ3H1GrMehXRf8cO97xTN",
      "metrics": {
        "step": 88,
        "train_loss": 0.478,
        "train_mean_token_accuracy": 0.924,
        "valid_loss": 10.112,
        "valid_mean_token_accuracy": 0.145,
        "full_valid_loss": 0.567,
        "full_valid_mean_token_accuracy": 0.944
      },
      "step_number": 88
    }

[

Batch
-----

](/docs/api-reference/batch)

Create large batches of API requests for asynchronous processing. The Batch API returns completions within 24 hours for a 50% discount.

Related guide: [Batch](/docs/guides/batch)

[

Create batch
------------

](/docs/api-reference/batch/create)

post https://api.openai.com/v1/batches

Creates and executes a batch from an uploaded file of requests

### Request body

[](#batch-create-input_file_id)

input\_file\_id

string

Required

The ID of an uploaded file that contains requests for the new batch.

See [upload file](/docs/api-reference/files/create) for how to upload a file.

Your input file must be formatted as a [JSONL file](/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 100 MB in size.

[](#batch-create-endpoint)

endpoint

string

Required

The endpoint to be used for all requests in the batch. Currently `/v1/chat/completions`, `/v1/embeddings`, and `/v1/completions` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

[](#batch-create-completion_window)

completion\_window

string

Required

The time frame within which the batch should be processed. Currently only `24h` is supported.

[](#batch-create-metadata)

metadata

object or null

Optional

Optional custom metadata for the batch.

### Returns

The created [Batch](/docs/api-reference/batch/object) object.

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    4
    5
    6
    7
    8
    curl https://api.openai.com/v1/batches \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "input_file_id": "file-abc123",
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    {
      "id": "batch_abc123",
      "object": "batch",
      "endpoint": "/v1/chat/completions",
      "errors": null,
      "input_file_id": "file-abc123",
      "completion_window": "24h",
      "status": "validating",
      "output_file_id": null,
      "error_file_id": null,
      "created_at": 1711471533,
      "in_progress_at": null,
      "expires_at": null,
      "finalizing_at": null,
      "completed_at": null,
      "failed_at": null,
      "expired_at": null,
      "cancelling_at": null,
      "cancelled_at": null,
      "request_counts": {
        "total": 0,
        "completed": 0,
        "failed": 0
      },
      "metadata": {
        "customer_id": "user_123456789",
        "batch_description": "Nightly eval job",
      }
    }

[

Retrieve batch
--------------

](/docs/api-reference/batch/retrieve)

get https://api.openai.com/v1/batches/{batch\_id}

Retrieves a batch.

### Path parameters

[](#batch-retrieve-batch_id)

batch\_id

string

Required

The ID of the batch to retrieve.

### Returns

The [Batch](/docs/api-reference/batch/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    curl https://api.openai.com/v1/batches/batch_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    {
      "id": "batch_abc123",
      "object": "batch",
      "endpoint": "/v1/completions",
      "errors": null,
      "input_file_id": "file-abc123",
      "completion_window": "24h",
      "status": "completed",
      "output_file_id": "file-cvaTdG",
      "error_file_id": "file-HOWS94",
      "created_at": 1711471533,
      "in_progress_at": 1711471538,
      "expires_at": 1711557933,
      "finalizing_at": 1711493133,
      "completed_at": 1711493163,
      "failed_at": null,
      "expired_at": null,
      "cancelling_at": null,
      "cancelled_at": null,
      "request_counts": {
        "total": 100,
        "completed": 95,
        "failed": 5
      },
      "metadata": {
        "customer_id": "user_123456789",
        "batch_description": "Nightly eval job",
      }
    }

[

Cancel batch
------------

](/docs/api-reference/batch/cancel)

post https://api.openai.com/v1/batches/{batch\_id}/cancel

Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.

### Path parameters

[](#batch-cancel-batch_id)

batch\_id

string

Required

The ID of the batch to cancel.

### Returns

The [Batch](/docs/api-reference/batch/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    4
    curl https://api.openai.com/v1/batches/batch_abc123/cancel \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -X POST

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    {
      "id": "batch_abc123",
      "object": "batch",
      "endpoint": "/v1/chat/completions",
      "errors": null,
      "input_file_id": "file-abc123",
      "completion_window": "24h",
      "status": "cancelling",
      "output_file_id": null,
      "error_file_id": null,
      "created_at": 1711471533,
      "in_progress_at": 1711471538,
      "expires_at": 1711557933,
      "finalizing_at": null,
      "completed_at": null,
      "failed_at": null,
      "expired_at": null,
      "cancelling_at": 1711475133,
      "cancelled_at": null,
      "request_counts": {
        "total": 100,
        "completed": 23,
        "failed": 1
      },
      "metadata": {
        "customer_id": "user_123456789",
        "batch_description": "Nightly eval job",
      }
    }

[

List batch
----------

](/docs/api-reference/batch/list)

get https://api.openai.com/v1/batches

List your organization's batches.

### Query parameters

[](#batch-list-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#batch-list-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

### Returns

A list of paginated [Batch](/docs/api-reference/batch/object) objects.

Example request

curl

Select librarycurlpythonnode

    1
    2
    3
    curl https://api.openai.com/v1/batches?limit=2 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    {
      "object": "list",
      "data": [
        {
          "id": "batch_abc123",
          "object": "batch",
          "endpoint": "/v1/chat/completions",
          "errors": null,
          "input_file_id": "file-abc123",
          "completion_window": "24h",
          "status": "completed",
          "output_file_id": "file-cvaTdG",
          "error_file_id": "file-HOWS94",
          "created_at": 1711471533,
          "in_progress_at": 1711471538,
          "expires_at": 1711557933,
          "finalizing_at": 1711493133,
          "completed_at": 1711493163,
          "failed_at": null,
          "expired_at": null,
          "cancelling_at": null,
          "cancelled_at": null,
          "request_counts": {
            "total": 100,
            "completed": 95,
            "failed": 5
          },
          "metadata": {
            "customer_id": "user_123456789",
            "batch_description": "Nightly job",
          }
        },
        { ... },
      ],
      "first_id": "batch_abc123",
      "last_id": "batch_abc456",
      "has_more": true
    }

[

The batch object
----------------

](/docs/api-reference/batch/object)

[](#batch/object-id)

id

string

[](#batch/object-object)

object

string

The object type, which is always `batch`.

[](#batch/object-endpoint)

endpoint

string

The OpenAI API endpoint used by the batch.

[](#batch/object-errors)

errors

object

Show properties

[](#batch/object-input_file_id)

input\_file\_id

string

The ID of the input file for the batch.

[](#batch/object-completion_window)

completion\_window

string

The time frame within which the batch should be processed.

[](#batch/object-status)

status

string

The current status of the batch.

[](#batch/object-output_file_id)

output\_file\_id

string

The ID of the file containing the outputs of successfully executed requests.

[](#batch/object-error_file_id)

error\_file\_id

string

The ID of the file containing the outputs of requests with errors.

[](#batch/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the batch was created.

[](#batch/object-in_progress_at)

in\_progress\_at

integer

The Unix timestamp (in seconds) for when the batch started processing.

[](#batch/object-expires_at)

expires\_at

integer

The Unix timestamp (in seconds) for when the batch will expire.

[](#batch/object-finalizing_at)

finalizing\_at

integer

The Unix timestamp (in seconds) for when the batch started finalizing.

[](#batch/object-completed_at)

completed\_at

integer

The Unix timestamp (in seconds) for when the batch was completed.

[](#batch/object-failed_at)

failed\_at

integer

The Unix timestamp (in seconds) for when the batch failed.

[](#batch/object-expired_at)

expired\_at

integer

The Unix timestamp (in seconds) for when the batch expired.

[](#batch/object-cancelling_at)

cancelling\_at

integer

The Unix timestamp (in seconds) for when the batch started cancelling.

[](#batch/object-cancelled_at)

cancelled\_at

integer

The Unix timestamp (in seconds) for when the batch was cancelled.

[](#batch/object-request_counts)

request\_counts

object

The request counts for different statuses within the batch.

Show properties

[](#batch/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The batch object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    {
      "id": "batch_abc123",
      "object": "batch",
      "endpoint": "/v1/completions",
      "errors": null,
      "input_file_id": "file-abc123",
      "completion_window": "24h",
      "status": "completed",
      "output_file_id": "file-cvaTdG",
      "error_file_id": "file-HOWS94",
      "created_at": 1711471533,
      "in_progress_at": 1711471538,
      "expires_at": 1711557933,
      "finalizing_at": 1711493133,
      "completed_at": 1711493163,
      "failed_at": null,
      "expired_at": null,
      "cancelling_at": null,
      "cancelled_at": null,
      "request_counts": {
        "total": 100,
        "completed": 95,
        "failed": 5
      },
      "metadata": {
        "customer_id": "user_123456789",
        "batch_description": "Nightly eval job",
      }
    }

[

The request input object
------------------------

](/docs/api-reference/batch/request-input)

The per-line object of the batch input file

[](#batch/request-input-custom_id)

custom\_id

string

A developer-provided per-request id that will be used to match outputs to inputs. Must be unique for each request in a batch.

[](#batch/request-input-method)

method

string

The HTTP method to be used for the request. Currently only `POST` is supported.

[](#batch/request-input-url)

url

string

The OpenAI API relative URL to be used for the request. Currently `/v1/chat/completions`, `/v1/embeddings`, and `/v1/completions` are supported.

The request input object

    {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is 2+2?"}]}}

[

The request output object
-------------------------

](/docs/api-reference/batch/request-output)

The per-line object of the batch output and error files

[](#batch/request-output-id)

id

string

[](#batch/request-output-custom_id)

custom\_id

string

A developer-provided per-request id that will be used to match outputs to inputs.

[](#batch/request-output-response)

response

object or null

Show properties

[](#batch/request-output-error)

error

object or null

For requests that failed with a non-HTTP error, this will contain more information on the cause of the failure.

Show properties

The request output object

    {"id": "batch_req_wnaDys", "custom_id": "request-2", "response": {"status_code": 200, "request_id": "req_c187b3", "body": {"id": "chatcmpl-9758Iw", "object": "chat.completion", "created": 1711475054, "model": "gpt-3.5-turbo", "choices": [{"index": 0, "message": {"role": "assistant", "content": "2 + 2 equals 4."}, "finish_reason": "stop"}], "usage": {"prompt_tokens": 24, "completion_tokens": 15, "total_tokens": 39}, "system_fingerprint": null}}, "error": null}

[

Files
-----

](/docs/api-reference/files)

Files are used to upload documents that can be used with features like [Assistants](/docs/api-reference/assistants), [Fine-tuning](/docs/api-reference/fine-tuning), and [Batch API](/docs/guides/batch).

[

Upload file
-----------

](/docs/api-reference/files/create)

post https://api.openai.com/v1/files

Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.

The Assistants API supports files up to 2 million tokens and of specific file types. See the [Assistants Tools guide](/docs/assistants/tools) for details.

The Fine-tuning API only supports `.jsonl` files. The input also has certain required formats for fine-tuning [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) models.

The Batch API only supports `.jsonl` files up to 100 MB in size. The input also has a specific required [format](/docs/api-reference/batch/request-input).

Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

### Request body

[](#files-create-file)

file

file

Required

The File object (not file name) to be uploaded.

[](#files-create-purpose)

purpose

string

Required

The intended purpose of the uploaded file.

Use "assistants" for [Assistants](/docs/api-reference/assistants) and [Message](/docs/api-reference/messages) files, "vision" for Assistants image file inputs, "batch" for [Batch API](/docs/guides/batch), and "fine-tune" for [Fine-tuning](/docs/api-reference/fine-tuning).

### Returns

The uploaded [File](/docs/api-reference/files/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/files \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -F purpose="fine-tune" \
      -F file="@mydata.jsonl"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 120000,
      "created_at": 1677610602,
      "filename": "mydata.jsonl",
      "purpose": "fine-tune",
    }

[

List files
----------

](/docs/api-reference/files/list)

get https://api.openai.com/v1/files

Returns a list of files that belong to the user's organization.

### Query parameters

[](#files-list-purpose)

purpose

string

Optional

Only return files with the given purpose.

### Returns

A list of [File](/docs/api-reference/files/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/files \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    {
      "data": [
        {
          "id": "file-abc123",
          "object": "file",
          "bytes": 175,
          "created_at": 1613677385,
          "filename": "salesOverview.pdf",
          "purpose": "assistants",
        },
        {
          "id": "file-abc123",
          "object": "file",
          "bytes": 140,
          "created_at": 1613779121,
          "filename": "puppy.jsonl",
          "purpose": "fine-tune",
        }
      ],
      "object": "list"
    }

[

Retrieve file
-------------

](/docs/api-reference/files/retrieve)

get https://api.openai.com/v1/files/{file\_id}

Returns information about a specific file.

### Path parameters

[](#files-retrieve-file_id)

file\_id

string

Required

The ID of the file to use for this request.

### Returns

The [File](/docs/api-reference/files/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/files/file-abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 120000,
      "created_at": 1677610602,
      "filename": "mydata.jsonl",
      "purpose": "fine-tune",
    }

[

Delete file
-----------

](/docs/api-reference/files/delete)

delete https://api.openai.com/v1/files/{file\_id}

Delete a file.

### Path parameters

[](#files-delete-file_id)

file\_id

string

Required

The ID of the file to use for this request.

### Returns

Deletion status.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    curl https://api.openai.com/v1/files/file-abc123 \
      -X DELETE \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    {
      "id": "file-abc123",
      "object": "file",
      "deleted": true
    }

[

Retrieve file content
---------------------

](/docs/api-reference/files/retrieve-contents)

get https://api.openai.com/v1/files/{file\_id}/content

Returns the contents of the specified file.

### Path parameters

[](#files-retrieve-contents-file_id)

file\_id

string

Required

The ID of the file to use for this request.

### Returns

The file content.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/files/file-abc123/content \
      -H "Authorization: Bearer $OPENAI_API_KEY" > file.jsonl

[

The file object
---------------

](/docs/api-reference/files/object)

The `File` object represents a document that has been uploaded to OpenAI.

[](#files/object-id)

id

string

The file identifier, which can be referenced in the API endpoints.

[](#files/object-bytes)

bytes

integer

The size of the file, in bytes.

[](#files/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the file was created.

[](#files/object-filename)

filename

string

The name of the file.

[](#files/object-object)

object

string

The object type, which is always `file`.

[](#files/object-purpose)

purpose

string

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results` and `vision`.

[](#files/object-status)

status

Deprecated

string

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

[](#files/object-status_details)

status\_details

Deprecated

string

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

The file object

    1
    2
    3
    4
    5
    6
    7
    8
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 120000,
      "created_at": 1677610602,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
    }

[

Images
------

](/docs/api-reference/images)

Given a prompt and/or an input image, the model will generate a new image.

Related guide: [Image generation](/docs/guides/images)

[

Create image
------------

](/docs/api-reference/images/create)

post https://api.openai.com/v1/images/generations

Creates an image given a prompt.

### Request body

[](#images-create-prompt)

prompt

string

Required

A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`.

[](#images-create-model)

model

string

Optional

Defaults to dall-e-2

The model to use for image generation.

[](#images-create-n)

n

integer or null

Optional

Defaults to 1

The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

[](#images-create-quality)

quality

string

Optional

Defaults to standard

The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`.

[](#images-create-response_format)

response\_format

string or null

Optional

Defaults to url

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

[](#images-create-size)

size

string or null

Optional

Defaults to 1024x1024

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.

[](#images-create-style)

style

string or null

Optional

Defaults to vivid

The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`.

[](#images-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a list of [image](/docs/api-reference/images/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    curl https://api.openai.com/v1/images/generations \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "dall-e-3",
        "prompt": "A cute baby sea otter",
        "n": 1,
        "size": "1024x1024"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    {
      "created": 1589478378,
      "data": [
        {
          "url": "https://..."
        },
        {
          "url": "https://..."
        }
      ]
    }

[

Create image edit
-----------------

](/docs/api-reference/images/createEdit)

post https://api.openai.com/v1/images/edits

Creates an edited or extended image given an original image and a prompt.

### Request body

[](#images-createedit-image)

image

file

Required

The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask.

[](#images-createedit-prompt)

prompt

string

Required

A text description of the desired image(s). The maximum length is 1000 characters.

[](#images-createedit-mask)

mask

file

Optional

An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.

[](#images-createedit-model)

model

string

Optional

Defaults to dall-e-2

The model to use for image generation. Only `dall-e-2` is supported at this time.

[](#images-createedit-n)

n

integer or null

Optional

Defaults to 1

The number of images to generate. Must be between 1 and 10.

[](#images-createedit-size)

size

string or null

Optional

Defaults to 1024x1024

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

[](#images-createedit-response_format)

response\_format

string or null

Optional

Defaults to url

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

[](#images-createedit-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a list of [image](/docs/api-reference/images/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/images/edits \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -F image="@otter.png" \
      -F mask="@mask.png" \
      -F prompt="A cute baby sea otter wearing a beret" \
      -F n=2 \
      -F size="1024x1024"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    {
      "created": 1589478378,
      "data": [
        {
          "url": "https://..."
        },
        {
          "url": "https://..."
        }
      ]
    }

[

Create image variation
----------------------

](/docs/api-reference/images/createVariation)

post https://api.openai.com/v1/images/variations

Creates a variation of a given image.

### Request body

[](#images-createvariation-image)

image

file

Required

The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.

[](#images-createvariation-model)

model

string

Optional

Defaults to dall-e-2

The model to use for image generation. Only `dall-e-2` is supported at this time.

[](#images-createvariation-n)

n

integer or null

Optional

Defaults to 1

The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

[](#images-createvariation-response_format)

response\_format

string or null

Optional

Defaults to url

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

[](#images-createvariation-size)

size

string or null

Optional

Defaults to 1024x1024

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

[](#images-createvariation-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a list of [image](/docs/api-reference/images/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/images/variations \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -F image="@otter.png" \
      -F n=2 \
      -F size="1024x1024"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    {
      "created": 1589478378,
      "data": [
        {
          "url": "https://..."
        },
        {
          "url": "https://..."
        }
      ]
    }

[

The image object
----------------

](/docs/api-reference/images/object)

Represents the url or the content of an image generated by the OpenAI API.

[](#images/object-b64_json)

b64\_json

string

The base64-encoded JSON of the generated image, if `response_format` is `b64_json`.

[](#images/object-url)

url

string

The URL of the generated image, if `response_format` is `url` (default).

[](#images/object-revised_prompt)

revised\_prompt

string

The prompt that was used to generate the image, if there was any revision to the prompt.

The image object

    1
    2
    3
    4
    {
      "url": "...",
      "revised_prompt": "..."
    }

[

Models
------

](/docs/api-reference/models)

List and describe the various models available in the API. You can refer to the [Models](/docs/models) documentation to understand what models are available and the differences between them.

[

List models
-----------

](/docs/api-reference/models/list)

get https://api.openai.com/v1/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Returns

A list of [model](/docs/api-reference/models/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/models \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    {
      "object": "list",
      "data": [
        {
          "id": "model-id-0",
          "object": "model",
          "created": 1686935002,
          "owned_by": "organization-owner"
        },
        {
          "id": "model-id-1",
          "object": "model",
          "created": 1686935002,
          "owned_by": "organization-owner",
        },
        {
          "id": "model-id-2",
          "object": "model",
          "created": 1686935002,
          "owned_by": "openai"
        },
      ],
      "object": "list"
    }

[

Retrieve model
--------------

](/docs/api-reference/models/retrieve)

get https://api.openai.com/v1/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Path parameters

[](#models-retrieve-model)

model

string

Required

The ID of the model to use for this request

### Returns

The [model](/docs/api-reference/models/object) object matching the specified ID.

Example request

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

curl

Select librarycurlpythonnode.js

    1
    2
    curl https://api.openai.com/v1/models/gpt-3.5-turbo-instruct \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

    1
    2
    3
    4
    5
    6
    {
      "id": "gpt-3.5-turbo-instruct",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
    }

[

Delete a fine-tuned model
-------------------------

](/docs/api-reference/models/delete)

delete https://api.openai.com/v1/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

### Path parameters

[](#models-delete-model)

model

string

Required

The model to delete

### Returns

Deletion status.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    curl https://api.openai.com/v1/models/ft:gpt-3.5-turbo:acemeco:suffix:abc123 \
      -X DELETE \
      -H "Authorization: Bearer $OPENAI_API_KEY"

Response

    1
    2
    3
    4
    5
    {
      "id": "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
      "object": "model",
      "deleted": true
    }

[

The model object
----------------

](/docs/api-reference/models/object)

Describes an OpenAI model offering that can be used with the API.

[](#models/object-id)

id

string

The model identifier, which can be referenced in the API endpoints.

[](#models/object-created)

created

integer

The Unix timestamp (in seconds) when the model was created.

[](#models/object-object)

object

string

The object type, which is always "model".

[](#models/object-owned_by)

owned\_by

string

The organization that owns the model.

The model object

gpt-3.5-turbo-instructgpt-4ogpt-3.5-turbo

    1
    2
    3
    4
    5
    6
    {
      "id": "davinci",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
    }

[

Moderations
-----------

](/docs/api-reference/moderations)

Given some input text, outputs if the model classifies it as potentially harmful across several categories.

Related guide: [Moderations](/docs/guides/moderation)

[

Create moderation
-----------------

](/docs/api-reference/moderations/create)

post https://api.openai.com/v1/moderations

Classifies if text is potentially harmful.

### Request body

[](#moderations-create-input)

input

string or array

Required

The input text to classify

[](#moderations-create-model)

model

string

Optional

Defaults to text-moderation-latest

Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.

### Returns

A [moderation](/docs/api-reference/moderations/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    curl https://api.openai.com/v1/moderations \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "input": "I want to kill them."
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    {
      "id": "modr-XXXXX",
      "model": "text-moderation-005",
      "results": [
        {
          "flagged": true,
          "categories": {
            "sexual": false,
            "hate": false,
            "harassment": false,
            "self-harm": false,
            "sexual/minors": false,
            "hate/threatening": false,
            "violence/graphic": false,
            "self-harm/intent": false,
            "self-harm/instructions": false,
            "harassment/threatening": true,
            "violence": true,
          },
          "category_scores": {
            "sexual": 1.2282071e-06,
            "hate": 0.010696256,
            "harassment": 0.29842457,
            "self-harm": 1.5236925e-08,
            "sexual/minors": 5.7246268e-08,
            "hate/threatening": 0.0060676364,
            "violence/graphic": 4.435014e-06,
            "self-harm/intent": 8.098441e-10,
            "self-harm/instructions": 2.8498655e-11,
            "harassment/threatening": 0.63055265,
            "violence": 0.99011886,
          }
        }
      ]
    }

[

The moderation object
---------------------

](/docs/api-reference/moderations/object)

Represents if a given text input is potentially harmful.

[](#moderations/object-id)

id

string

The unique identifier for the moderation request.

[](#moderations/object-model)

model

string

The model used to generate the moderation results.

[](#moderations/object-results)

results

array

A list of moderation objects.

Show properties

The moderation object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    {
      "id": "modr-XXXXX",
      "model": "text-moderation-005",
      "results": [
        {
          "flagged": true,
          "categories": {
            "sexual": false,
            "hate": false,
            "harassment": false,
            "self-harm": false,
            "sexual/minors": false,
            "hate/threatening": false,
            "violence/graphic": false,
            "self-harm/intent": false,
            "self-harm/instructions": false,
            "harassment/threatening": true,
            "violence": true,
          },
          "category_scores": {
            "sexual": 1.2282071e-06,
            "hate": 0.010696256,
            "harassment": 0.29842457,
            "self-harm": 1.5236925e-08,
            "sexual/minors": 5.7246268e-08,
            "hate/threatening": 0.0060676364,
            "violence/graphic": 4.435014e-06,
            "self-harm/intent": 8.098441e-10,
            "self-harm/instructions": 2.8498655e-11,
            "harassment/threatening": 0.63055265,
            "violence": 0.99011886,
          }
        }
      ]
    }

[

Assistants

Beta


------------------

](/docs/api-reference/assistants)

Build assistants that can call models and use tools to perform tasks.

[Get started with the Assistants API](/docs/assistants)

[

Create assistant

Beta


------------------------

](/docs/api-reference/assistants/createAssistant)

post https://api.openai.com/v1/assistants

Create an assistant with a model and instructions.

### Request body

[](#assistants-createassistant-model)

model

string

Required

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

[](#assistants-createassistant-name)

name

string or null

Optional

The name of the assistant. The maximum length is 256 characters.

[](#assistants-createassistant-description)

description

string or null

Optional

The description of the assistant. The maximum length is 512 characters.

[](#assistants-createassistant-instructions)

instructions

string or null

Optional

The system instructions that the assistant uses. The maximum length is 256,000 characters.

[](#assistants-createassistant-tools)

tools

array

Optional

Defaults to \[\]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

Show possible types

[](#assistants-createassistant-tool_resources)

tool\_resources

object or null

Optional

A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#assistants-createassistant-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#assistants-createassistant-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#assistants-createassistant-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#assistants-createassistant-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

An [assistant](/docs/api-reference/assistants/object) object.

Code Interpreter‍Files‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl "https://api.openai.com/v1/assistants" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
        "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        "name": "Math Tutor",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-turbo"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1698984975,
      "name": "Math Tutor",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

List assistants

Beta


-----------------------

](/docs/api-reference/assistants/listAssistants)

get https://api.openai.com/v1/assistants

Returns a list of assistants.

### Query parameters

[](#assistants-listassistants-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#assistants-listassistants-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#assistants-listassistants-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#assistants-listassistants-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [assistant](/docs/api-reference/assistants/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl "https://api.openai.com/v1/assistants?order=desc&limit=20" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    {
      "object": "list",
      "data": [
        {
          "id": "asst_abc123",
          "object": "assistant",
          "created_at": 1698982736,
          "name": "Coding Tutor",
          "description": null,
          "model": "gpt-4-turbo",
          "instructions": "You are a helpful assistant designed to make me better at coding!",
          "tools": [],
          "tool_resources": {},
          "metadata": {},
          "top_p": 1.0,
          "temperature": 1.0,
          "response_format": "auto"
        },
        {
          "id": "asst_abc456",
          "object": "assistant",
          "created_at": 1698982718,
          "name": "My Assistant",
          "description": null,
          "model": "gpt-4-turbo",
          "instructions": "You are a helpful assistant designed to make me better at coding!",
          "tools": [],
          "tool_resources": {},
          "metadata": {},
          "top_p": 1.0,
          "temperature": 1.0,
          "response_format": "auto"
        },
        {
          "id": "asst_abc789",
          "object": "assistant",
          "created_at": 1698982643,
          "name": null,
          "description": null,
          "model": "gpt-4-turbo",
          "instructions": null,
          "tools": [],
          "tool_resources": {},
          "metadata": {},
          "top_p": 1.0,
          "temperature": 1.0,
          "response_format": "auto"
        }
      ],
      "first_id": "asst_abc123",
      "last_id": "asst_abc789",
      "has_more": false
    }

[

Retrieve assistant

Beta


--------------------------

](/docs/api-reference/assistants/getAssistant)

get https://api.openai.com/v1/assistants/{assistant\_id}

Retrieves an assistant.

### Path parameters

[](#assistants-getassistant-assistant_id)

assistant\_id

string

Required

The ID of the assistant to retrieve.

### Returns

The [assistant](/docs/api-reference/assistants/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/assistants/asst_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1699009709,
      "name": "HR Helper",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies.",
      "tools": [
        {
          "type": "file_search"
        }
      ],
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

Modify assistant

Beta


------------------------

](/docs/api-reference/assistants/modifyAssistant)

post https://api.openai.com/v1/assistants/{assistant\_id}

Modifies an assistant.

### Path parameters

[](#assistants-modifyassistant-assistant_id)

assistant\_id

string

Required

The ID of the assistant to modify.

### Request body

[](#assistants-modifyassistant-model)

model

Optional

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

[](#assistants-modifyassistant-name)

name

string or null

Optional

The name of the assistant. The maximum length is 256 characters.

[](#assistants-modifyassistant-description)

description

string or null

Optional

The description of the assistant. The maximum length is 512 characters.

[](#assistants-modifyassistant-instructions)

instructions

string or null

Optional

The system instructions that the assistant uses. The maximum length is 256,000 characters.

[](#assistants-modifyassistant-tools)

tools

array

Optional

Defaults to \[\]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

Show possible types

[](#assistants-modifyassistant-tool_resources)

tool\_resources

object or null

Optional

A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#assistants-modifyassistant-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#assistants-modifyassistant-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#assistants-modifyassistant-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#assistants-modifyassistant-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

The modified [assistant](/docs/api-reference/assistants/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    curl https://api.openai.com/v1/assistants/asst_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
          "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
          "tools": [{"type": "file_search"}],
          "model": "gpt-4-turbo"
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    {
      "id": "asst_123",
      "object": "assistant",
      "created_at": 1699009709,
      "name": "HR Helper",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
      "tools": [
        {
          "type": "file_search"
        }
      ],
      "tool_resources": {
        "file_search": {
          "vector_store_ids": []
        }
      },
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

Delete assistant

Beta


------------------------

](/docs/api-reference/assistants/deleteAssistant)

delete https://api.openai.com/v1/assistants/{assistant\_id}

Delete an assistant.

### Path parameters

[](#assistants-deleteassistant-assistant_id)

assistant\_id

string

Required

The ID of the assistant to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/assistants/asst_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      "id": "asst_abc123",
      "object": "assistant.deleted",
      "deleted": true
    }

[

The assistant object

Beta


----------------------------

](/docs/api-reference/assistants/object)

Represents an `assistant` that can call the model and use tools.

[](#assistants/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#assistants/object-object)

object

string

The object type, which is always `assistant`.

[](#assistants/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the assistant was created.

[](#assistants/object-name)

name

string or null

The name of the assistant. The maximum length is 256 characters.

[](#assistants/object-description)

description

string or null

The description of the assistant. The maximum length is 512 characters.

[](#assistants/object-model)

model

string

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

[](#assistants/object-instructions)

instructions

string or null

The system instructions that the assistant uses. The maximum length is 256,000 characters.

[](#assistants/object-tools)

tools

array

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

Show possible types

[](#assistants/object-tool_resources)

tool\_resources

object or null

A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#assistants/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#assistants/object-temperature)

temperature

number or null

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#assistants/object-top_p)

top\_p

number or null

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#assistants/object-response_format)

response\_format

string or object

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

The assistant object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1698984975,
      "name": "Math Tutor",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

Threads

Beta


---------------

](/docs/api-reference/threads)

Create threads that assistants can interact with.

Related guide: [Assistants](/docs/assistants/overview)

[

Create thread

Beta


---------------------

](/docs/api-reference/threads/createThread)

post https://api.openai.com/v1/threads

Create a thread.

### Request body

[](#threads-createthread-messages)

messages

array

Optional

A list of [messages](/docs/api-reference/messages) to start the thread with.

Show properties

[](#threads-createthread-tool_resources)

tool\_resources

object or null

Optional

A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#threads-createthread-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [thread](/docs/api-reference/threads) object.

Empty‍Messages‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/threads \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -d ''

Response

    1
    2
    3
    4
    5
    6
    7
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1699012949,
      "metadata": {},
      "tool_resources": {}
    }

[

Retrieve thread

Beta


-----------------------

](/docs/api-reference/threads/getThread)

get https://api.openai.com/v1/threads/{thread\_id}

Retrieves a thread.

### Path parameters

[](#threads-getthread-thread_id)

thread\_id

string

Required

The ID of the thread to retrieve.

### Returns

The [thread](/docs/api-reference/threads/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1699014083,
      "metadata": {},
      "tool_resources": {
        "code_interpreter": {
          "file_ids": []
        }
      }
    }

[

Modify thread

Beta


---------------------

](/docs/api-reference/threads/modifyThread)

post https://api.openai.com/v1/threads/{thread\_id}

Modifies a thread.

### Path parameters

[](#threads-modifythread-thread_id)

thread\_id

string

Required

The ID of the thread to modify. Only the `metadata` can be modified.

### Request body

[](#threads-modifythread-tool_resources)

tool\_resources

object or null

Optional

A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#threads-modifythread-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [thread](/docs/api-reference/threads/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl https://api.openai.com/v1/threads/thread_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
          "metadata": {
            "modified": "true",
            "user": "abc123"
          }
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1699014083,
      "metadata": {
        "modified": "true",
        "user": "abc123"
      },
      "tool_resources": {}
    }

[

Delete thread

Beta


---------------------

](/docs/api-reference/threads/deleteThread)

delete https://api.openai.com/v1/threads/{thread\_id}

Delete a thread.

### Path parameters

[](#threads-deletethread-thread_id)

thread\_id

string

Required

The ID of the thread to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/threads/thread_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      "id": "thread_abc123",
      "object": "thread.deleted",
      "deleted": true
    }

[

The thread object

Beta


-------------------------

](/docs/api-reference/threads/object)

Represents a thread that contains [messages](/docs/api-reference/messages).

[](#threads/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#threads/object-object)

object

string

The object type, which is always `thread`.

[](#threads/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the thread was created.

[](#threads/object-tool_resources)

tool\_resources

object or null

A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#threads/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The thread object

    1
    2
    3
    4
    5
    6
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1698107661,
      "metadata": {}
    }

[

Messages

Beta


----------------

](/docs/api-reference/messages)

Create messages within threads

Related guide: [Assistants](/docs/assistants/overview)

[

Create message

Beta


----------------------

](/docs/api-reference/messages/createMessage)

post https://api.openai.com/v1/threads/{thread\_id}/messages

Create a message.

### Path parameters

[](#messages-createmessage-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads) to create a message for.

### Request body

[](#messages-createmessage-role)

role

string

Required

The role of the entity that is creating the message. Allowed values include:

*   `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
*   `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

[](#messages-createmessage-content)

content

string or array

Required

Show possible types

[](#messages-createmessage-attachments)

attachments

array or null

Optional

A list of files attached to the message, and the tools they should be added to.

Show properties

[](#messages-createmessage-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [message](/docs/api-reference/messages/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    curl https://api.openai.com/v1/threads/thread_abc123/messages \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
          "role": "user",
          "content": "How does AI work? Explain it in simple terms."
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1713226573,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "attachments": [],
      "metadata": {}
    }

[

List messages

Beta


---------------------

](/docs/api-reference/messages/listMessages)

get https://api.openai.com/v1/threads/{thread\_id}/messages

Returns a list of messages for a given thread.

### Path parameters

[](#messages-listmessages-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads) the messages belong to.

### Query parameters

[](#messages-listmessages-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#messages-listmessages-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#messages-listmessages-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#messages-listmessages-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

[](#messages-listmessages-run_id)

run\_id

string

Optional

Filter messages by the run ID that generated them.

### Returns

A list of [message](/docs/api-reference/messages) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/messages \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    {
      "object": "list",
      "data": [
        {
          "id": "msg_abc123",
          "object": "thread.message",
          "created_at": 1699016383,
          "assistant_id": null,
          "thread_id": "thread_abc123",
          "run_id": null,
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": {
                "value": "How does AI work? Explain it in simple terms.",
                "annotations": []
              }
            }
          ],
          "attachments": [],
          "metadata": {}
        },
        {
          "id": "msg_abc456",
          "object": "thread.message",
          "created_at": 1699016383,
          "assistant_id": null,
          "thread_id": "thread_abc123",
          "run_id": null,
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": {
                "value": "Hello, what is AI?",
                "annotations": []
              }
            }
          ],
          "attachments": [],
          "metadata": {}
        }
      ],
      "first_id": "msg_abc123",
      "last_id": "msg_abc456",
      "has_more": false
    }

[

Retrieve message

Beta


------------------------

](/docs/api-reference/messages/getMessage)

get https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}

Retrieve a message.

### Path parameters

[](#messages-getmessage-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads) to which this message belongs.

[](#messages-getmessage-message_id)

message\_id

string

Required

The ID of the message to retrieve.

### Returns

The [message](/docs/api-reference/threads/messages/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699017614,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "attachments": [],
      "metadata": {}
    }

[

Modify message

Beta


----------------------

](/docs/api-reference/messages/modifyMessage)

post https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}

Modifies a message.

### Path parameters

[](#messages-modifymessage-thread_id)

thread\_id

string

Required

The ID of the thread to which this message belongs.

[](#messages-modifymessage-message_id)

message\_id

string

Required

The ID of the message to modify.

### Request body

[](#messages-modifymessage-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [message](/docs/api-reference/threads/messages/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
          "metadata": {
            "modified": "true",
            "user": "abc123"
          }
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699017614,
      "assistant_id": null,
      "thread_id": "thread_abc123",
      "run_id": null,
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "file_ids": [],
      "metadata": {
        "modified": "true",
        "user": "abc123"
      }
    }

[

Delete message

Beta


----------------------

](/docs/api-reference/messages/deleteMessage)

delete https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

### Path parameters

[](#messages-deletemessage-thread_id)

thread\_id

string

Required

The ID of the thread to which this message belongs.

[](#messages-deletemessage-message_id)

message\_id

string

Required

The ID of the message to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl -X DELETE https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    {
      "id": "msg_abc123",
      "object": "thread.message.deleted",
      "deleted": true
    }

[

The message object

Beta


--------------------------

](/docs/api-reference/messages/object)

Represents a message within a [thread](/docs/api-reference/threads).

[](#messages/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#messages/object-object)

object

string

The object type, which is always `thread.message`.

[](#messages/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the message was created.

[](#messages/object-thread_id)

thread\_id

string

The [thread](/docs/api-reference/threads) ID that this message belongs to.

[](#messages/object-status)

status

string

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

[](#messages/object-incomplete_details)

incomplete\_details

object or null

On an incomplete message, details about why the message is incomplete.

Show properties

[](#messages/object-completed_at)

completed\_at

integer or null

The Unix timestamp (in seconds) for when the message was completed.

[](#messages/object-incomplete_at)

incomplete\_at

integer or null

The Unix timestamp (in seconds) for when the message was marked as incomplete.

[](#messages/object-role)

role

string

The entity that produced the message. One of `user` or `assistant`.

[](#messages/object-content)

content

array

The content of the message in array of text and/or images.

Show possible types

[](#messages/object-assistant_id)

assistant\_id

string or null

If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message.

[](#messages/object-run_id)

run\_id

string or null

The ID of the [run](/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

[](#messages/object-attachments)

attachments

array or null

A list of files attached to the message, and the tools they were added to.

Show properties

[](#messages/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The message object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1698983503,
      "thread_id": "thread_abc123",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "Hi! How can I help you today?",
            "annotations": []
          }
        }
      ],
      "assistant_id": "asst_abc123",
      "run_id": "run_abc123",
      "attachments": [],
      "metadata": {}
    }

[

Runs

Beta


------------

](/docs/api-reference/runs)

Represents an execution run on a thread.

Related guide: [Assistants](/docs/assistants/overview)

[

Create run

Beta


------------------

](/docs/api-reference/runs/createRun)

post https://api.openai.com/v1/threads/{thread\_id}/runs

Create a run.

### Path parameters

[](#runs-createrun-thread_id)

thread\_id

string

Required

The ID of the thread to run.

### Request body

[](#runs-createrun-assistant_id)

assistant\_id

string

Required

The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

[](#runs-createrun-model)

model

string

Optional

The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

[](#runs-createrun-instructions)

instructions

string or null

Optional

Overrides the [instructions](/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

[](#runs-createrun-additional_instructions)

additional\_instructions

string or null

Optional

Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

[](#runs-createrun-additional_messages)

additional\_messages

array or null

Optional

Adds additional messages to the thread before creating the run.

Show properties

[](#runs-createrun-tools)

tools

array or null

Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

Show possible types

[](#runs-createrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs-createrun-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#runs-createrun-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#runs-createrun-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

[](#runs-createrun-max_prompt_tokens)

max\_prompt\_tokens

integer or null

Optional

The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

[](#runs-createrun-max_completion_tokens)

max\_completion\_tokens

integer or null

Optional

The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

[](#runs-createrun-truncation_strategy)

truncation\_strategy

object

Optional

Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run.

Show properties

[](#runs-createrun-tool_choice)

tool\_choice

string or object

Optional

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Show possible types

[](#runs-createrun-parallel_tool_calls)

parallel\_tool\_calls

boolean

Optional

Defaults to true

Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.

[](#runs-createrun-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

A [run](/docs/api-reference/runs/object) object.

Default‍Streaming‍Streaming with Functions‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/threads/thread_abc123/runs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
        "assistant_id": "asst_abc123"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699063290,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "queued",
      "started_at": 1699063290,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699063291,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "metadata": {},
      "usage": null,
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

Create thread and run

Beta


-----------------------------

](/docs/api-reference/runs/createThreadAndRun)

post https://api.openai.com/v1/threads/runs

Create a thread and run it in one request.

### Request body

[](#runs-createthreadandrun-assistant_id)

assistant\_id

string

Required

The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

[](#runs-createthreadandrun-thread)

thread

object

Optional

Show properties

[](#runs-createthreadandrun-model)

model

string

Optional

The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

[](#runs-createthreadandrun-instructions)

instructions

string or null

Optional

Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

[](#runs-createthreadandrun-tools)

tools

array or null

Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

[](#runs-createthreadandrun-tool_resources)

tool\_resources

object or null

Optional

A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Show properties

[](#runs-createthreadandrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs-createthreadandrun-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#runs-createthreadandrun-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#runs-createthreadandrun-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

[](#runs-createthreadandrun-max_prompt_tokens)

max\_prompt\_tokens

integer or null

Optional

The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

[](#runs-createthreadandrun-max_completion_tokens)

max\_completion\_tokens

integer or null

Optional

The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

[](#runs-createthreadandrun-truncation_strategy)

truncation\_strategy

object

Optional

Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run.

Show properties

[](#runs-createthreadandrun-tool_choice)

tool\_choice

string or object

Optional

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Show possible types

[](#runs-createthreadandrun-parallel_tool_calls)

parallel\_tool\_calls

boolean

Optional

Defaults to true

Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.

[](#runs-createthreadandrun-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

A [run](/docs/api-reference/runs/object) object.

Default‍Streaming‍Streaming with Functions‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    curl https://api.openai.com/v1/threads/runs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
          "assistant_id": "asst_abc123",
          "thread": {
            "messages": [
              {"role": "user", "content": "Explain deep learning to a 5 year old."}
            ]
          }
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699076792,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "queued",
      "started_at": null,
      "expires_at": 1699077392,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": null,
      "required_action": null,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": "You are a helpful assistant.",
      "tools": [],
      "tool_resources": {},
      "metadata": {},
      "temperature": 1.0,
      "top_p": 1.0,
      "max_completion_tokens": null,
      "max_prompt_tokens": null,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "incomplete_details": null,
      "usage": null,
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

List runs

Beta


-----------------

](/docs/api-reference/runs/listRuns)

get https://api.openai.com/v1/threads/{thread\_id}/runs

Returns a list of runs belonging to a thread.

### Path parameters

[](#runs-listruns-thread_id)

thread\_id

string

Required

The ID of the thread the run belongs to.

### Query parameters

[](#runs-listruns-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#runs-listruns-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#runs-listruns-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#runs-listruns-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [run](/docs/api-reference/runs/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74
    75
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87
    88
    89
    90
    91
    92
    93
    94
    95
    96
    97
    98
    99
    100
    101
    102
    {
      "object": "list",
      "data": [
        {
          "id": "run_abc123",
          "object": "thread.run",
          "created_at": 1699075072,
          "assistant_id": "asst_abc123",
          "thread_id": "thread_abc123",
          "status": "completed",
          "started_at": 1699075072,
          "expires_at": null,
          "cancelled_at": null,
          "failed_at": null,
          "completed_at": 1699075073,
          "last_error": null,
          "model": "gpt-4-turbo",
          "instructions": null,
          "incomplete_details": null,
          "tools": [
            {
              "type": "code_interpreter"
            }
          ],
          "tool_resources": {
            "code_interpreter": {
              "file_ids": [
                "file-abc123",
                "file-abc456"
              ]
            }
          },
          "metadata": {},
          "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 456,
            "total_tokens": 579
          },
          "temperature": 1.0,
          "top_p": 1.0,
          "max_prompt_tokens": 1000,
          "max_completion_tokens": 1000,
          "truncation_strategy": {
            "type": "auto",
            "last_messages": null
          },
          "response_format": "auto",
          "tool_choice": "auto",
          "parallel_tool_calls": true
        },
        {
          "id": "run_abc456",
          "object": "thread.run",
          "created_at": 1699063290,
          "assistant_id": "asst_abc123",
          "thread_id": "thread_abc123",
          "status": "completed",
          "started_at": 1699063290,
          "expires_at": null,
          "cancelled_at": null,
          "failed_at": null,
          "completed_at": 1699063291,
          "last_error": null,
          "model": "gpt-4-turbo",
          "instructions": null,
          "incomplete_details": null,
          "tools": [
            {
              "type": "code_interpreter"
            }
          ],
          "tool_resources": {
            "code_interpreter": {
              "file_ids": [
                "file-abc123",
                "file-abc456"
              ]
            }
          },
          "metadata": {},
          "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 456,
            "total_tokens": 579
          },
          "temperature": 1.0,
          "top_p": 1.0,
          "max_prompt_tokens": 1000,
          "max_completion_tokens": 1000,
          "truncation_strategy": {
            "type": "auto",
            "last_messages": null
          },
          "response_format": "auto",
          "tool_choice": "auto",
          "parallel_tool_calls": true
        }
      ],
      "first_id": "run_abc123",
      "last_id": "run_abc456",
      "has_more": false
    }

[

Retrieve run

Beta


--------------------

](/docs/api-reference/runs/getRun)

get https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}

Retrieves a run.

### Path parameters

[](#runs-getrun-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads) that was run.

[](#runs-getrun-run_id)

run\_id

string

Required

The ID of the run to retrieve.

### Returns

The [run](/docs/api-reference/runs/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

Modify run

Beta


------------------

](/docs/api-reference/runs/modifyRun)

post https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}

Modifies a run.

### Path parameters

[](#runs-modifyrun-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads) that was run.

[](#runs-modifyrun-run_id)

run\_id

string

Required

The ID of the run to modify.

### Request body

[](#runs-modifyrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [run](/docs/api-reference/runs/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
        "metadata": {
          "user_id": "user_abc123"
        }
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "tool_resources": {
        "code_interpreter": {
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ]
        }
      },
      "metadata": {
        "user_id": "user_abc123"
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

Submit tool outputs to run

Beta


----------------------------------

](/docs/api-reference/runs/submitToolOutputs)

post https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.

### Path parameters

[](#runs-submittooloutputs-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads) to which this run belongs.

[](#runs-submittooloutputs-run_id)

run\_id

string

Required

The ID of the run that requires the tool output submission.

### Request body

[](#runs-submittooloutputs-tool_outputs)

tool\_outputs

array

Required

A list of tools for which the outputs are being submitted.

Show properties

[](#runs-submittooloutputs-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

### Returns

The modified [run](/docs/api-reference/runs/object) object matching the specified ID.

Default‍Streaming‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    curl https://api.openai.com/v1/threads/thread_123/runs/run_123/submit_tool_outputs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -d '{
        "tool_outputs": [
          {
            "tool_call_id": "call_001",
            "output": "70 degrees and sunny."
          }
        ]
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    {
      "id": "run_123",
      "object": "thread.run",
      "created_at": 1699075592,
      "assistant_id": "asst_123",
      "thread_id": "thread_123",
      "status": "queued",
      "started_at": 1699075592,
      "expires_at": 1699076192,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": null,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"]
                }
              },
              "required": ["location"]
            }
          }
        }
      ],
      "metadata": {},
      "usage": null,
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

Cancel a run

Beta


--------------------

](/docs/api-reference/runs/cancelRun)

post https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/cancel

Cancels a run that is `in_progress`.

### Path parameters

[](#runs-cancelrun-thread_id)

thread\_id

string

Required

The ID of the thread to which this run belongs.

[](#runs-cancelrun-run_id)

run\_id

string

Required

The ID of the run to cancel.

### Returns

The modified [run](/docs/api-reference/runs/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/cancel \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v2" \
      -X POST

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699076126,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "cancelling",
      "started_at": 1699076126,
      "expires_at": 1699076726,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": null,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": "You summarize books.",
      "tools": [
        {
          "type": "file_search"
        }
      ],
      "tool_resources": {
        "file_search": {
          "vector_store_ids": ["vs_123"]
        }
      },
      "metadata": {},
      "usage": null,
      "temperature": 1.0,
      "top_p": 1.0,
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

The run object

Beta


----------------------

](/docs/api-reference/runs/object)

Represents an execution run on a [thread](/docs/api-reference/threads).

[](#runs/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#runs/object-object)

object

string

The object type, which is always `thread.run`.

[](#runs/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the run was created.

[](#runs/object-thread_id)

thread\_id

string

The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.

[](#runs/object-assistant_id)

assistant\_id

string

The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.

[](#runs/object-status)

status

string

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

[](#runs/object-required_action)

required\_action

object or null

Details on the action required to continue the run. Will be `null` if no action is required.

Show properties

[](#runs/object-last_error)

last\_error

object or null

The last error associated with this run. Will be `null` if there are no errors.

Show properties

[](#runs/object-expires_at)

expires\_at

integer or null

The Unix timestamp (in seconds) for when the run will expire.

[](#runs/object-started_at)

started\_at

integer or null

The Unix timestamp (in seconds) for when the run was started.

[](#runs/object-cancelled_at)

cancelled\_at

integer or null

The Unix timestamp (in seconds) for when the run was cancelled.

[](#runs/object-failed_at)

failed\_at

integer or null

The Unix timestamp (in seconds) for when the run failed.

[](#runs/object-completed_at)

completed\_at

integer or null

The Unix timestamp (in seconds) for when the run was completed.

[](#runs/object-incomplete_details)

incomplete\_details

object or null

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

Show properties

[](#runs/object-model)

model

string

The model that the [assistant](/docs/api-reference/assistants) used for this run.

[](#runs/object-instructions)

instructions

string

The instructions that the [assistant](/docs/api-reference/assistants) used for this run.

[](#runs/object-tools)

tools

array

The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.

Show possible types

[](#runs/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs/object-usage)

usage

object or null

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

Show properties

[](#runs/object-temperature)

temperature

number or null

The sampling temperature used for this run. If not set, defaults to 1.

[](#runs/object-top_p)

top\_p

number or null

The nucleus sampling value used for this run. If not set, defaults to 1.

[](#runs/object-max_prompt_tokens)

max\_prompt\_tokens

integer or null

The maximum number of prompt tokens specified to have been used over the course of the run.

[](#runs/object-max_completion_tokens)

max\_completion\_tokens

integer or null

The maximum number of completion tokens specified to have been used over the course of the run.

[](#runs/object-truncation_strategy)

truncation\_strategy

object

Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run.

Show properties

[](#runs/object-tool_choice)

tool\_choice

string or object

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Show possible types

[](#runs/object-parallel_tool_calls)

parallel\_tool\_calls

boolean

Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.

[](#runs/object-response_format)

response\_format

string or object

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

The run object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1698107661,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699073476,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699073498,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "tools": [{"type": "file_search"}, {"type": "code_interpreter"}],
      "metadata": {},
      "incomplete_details": null,
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
    }

[

Run Steps

Beta


-----------------

](/docs/api-reference/run-steps)

Represents the steps (model and tool calls) taken during the run.

Related guide: [Assistants](/docs/assistants/overview)

[

List run steps

Beta


----------------------

](/docs/api-reference/run-steps/listRunSteps)

get https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/steps

Returns a list of run steps belonging to a run.

### Path parameters

[](#run-steps-listrunsteps-thread_id)

thread\_id

string

Required

The ID of the thread the run and run steps belong to.

[](#run-steps-listrunsteps-run_id)

run\_id

string

Required

The ID of the run the run steps belong to.

### Query parameters

[](#run-steps-listrunsteps-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#run-steps-listrunsteps-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#run-steps-listrunsteps-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#run-steps-listrunsteps-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [run step](/docs/api-reference/runs/step-object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/steps \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    {
      "object": "list",
      "data": [
        {
          "id": "step_abc123",
          "object": "thread.run.step",
          "created_at": 1699063291,
          "run_id": "run_abc123",
          "assistant_id": "asst_abc123",
          "thread_id": "thread_abc123",
          "type": "message_creation",
          "status": "completed",
          "cancelled_at": null,
          "completed_at": 1699063291,
          "expired_at": null,
          "failed_at": null,
          "last_error": null,
          "step_details": {
            "type": "message_creation",
            "message_creation": {
              "message_id": "msg_abc123"
            }
          },
          "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 456,
            "total_tokens": 579
          }
        }
      ],
      "first_id": "step_abc123",
      "last_id": "step_abc456",
      "has_more": false
    }

[

Retrieve run step

Beta


-------------------------

](/docs/api-reference/run-steps/getRunStep)

get https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

Retrieves a run step.

### Path parameters

[](#run-steps-getrunstep-thread_id)

thread\_id

string

Required

The ID of the thread to which the run and run step belongs.

[](#run-steps-getrunstep-run_id)

run\_id

string

Required

The ID of the run to which the run step belongs.

[](#run-steps-getrunstep-step_id)

step\_id

string

Required

The ID of the run step to retrieve.

### Returns

The [run step](/docs/api-reference/runs/step-object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/steps/step_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "created_at": 1699063291,
      "run_id": "run_abc123",
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "type": "message_creation",
      "status": "completed",
      "cancelled_at": null,
      "completed_at": 1699063291,
      "expired_at": null,
      "failed_at": null,
      "last_error": null,
      "step_details": {
        "type": "message_creation",
        "message_creation": {
          "message_id": "msg_abc123"
        }
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      }
    }

[

The run step object

Beta


---------------------------

](/docs/api-reference/run-steps/step-object)

Represents a step in execution of a run.

[](#run-steps/step-object-id)

id

string

The identifier of the run step, which can be referenced in API endpoints.

[](#run-steps/step-object-object)

object

string

The object type, which is always `thread.run.step`.

[](#run-steps/step-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the run step was created.

[](#run-steps/step-object-assistant_id)

assistant\_id

string

The ID of the [assistant](/docs/api-reference/assistants) associated with the run step.

[](#run-steps/step-object-thread_id)

thread\_id

string

The ID of the [thread](/docs/api-reference/threads) that was run.

[](#run-steps/step-object-run_id)

run\_id

string

The ID of the [run](/docs/api-reference/runs) that this run step is a part of.

[](#run-steps/step-object-type)

type

string

The type of run step, which can be either `message_creation` or `tool_calls`.

[](#run-steps/step-object-status)

status

string

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

[](#run-steps/step-object-step_details)

step\_details

object

The details of the run step.

Show possible types

[](#run-steps/step-object-last_error)

last\_error

object or null

The last error associated with this run step. Will be `null` if there are no errors.

Show properties

[](#run-steps/step-object-expired_at)

expired\_at

integer or null

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

[](#run-steps/step-object-cancelled_at)

cancelled\_at

integer or null

The Unix timestamp (in seconds) for when the run step was cancelled.

[](#run-steps/step-object-failed_at)

failed\_at

integer or null

The Unix timestamp (in seconds) for when the run step failed.

[](#run-steps/step-object-completed_at)

completed\_at

integer or null

The Unix timestamp (in seconds) for when the run step completed.

[](#run-steps/step-object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#run-steps/step-object-usage)

usage

object or null

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

Show properties

The run step object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "created_at": 1699063291,
      "run_id": "run_abc123",
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "type": "message_creation",
      "status": "completed",
      "cancelled_at": null,
      "completed_at": 1699063291,
      "expired_at": null,
      "failed_at": null,
      "last_error": null,
      "step_details": {
        "type": "message_creation",
        "message_creation": {
          "message_id": "msg_abc123"
        }
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      }
    }

[

Vector Stores

Beta


---------------------

](/docs/api-reference/vector-stores)

Vector stores are used to store files for use by the `file_search` tool.

Related guide: [File Search](/docs/assistants/tools/file-search)

[

Create vector store

Beta


---------------------------

](/docs/api-reference/vector-stores/create)

post https://api.openai.com/v1/vector\_stores

Create a vector store.

### Request body

[](#vector-stores-create-file_ids)

file\_ids

array

Optional

A list of [File](/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

[](#vector-stores-create-name)

name

string

Optional

The name of the vector store.

[](#vector-stores-create-expires_after)

expires\_after

object

Optional

The expiration policy for a vector store.

Show properties

[](#vector-stores-create-chunking_strategy)

chunking\_strategy

object

Optional

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

Show possible types

[](#vector-stores-create-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [vector store](/docs/api-reference/vector-stores/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/vector_stores \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"
      -d '{
        "name": "Support FAQ"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    {
      "id": "vs_abc123",
      "object": "vector_store",
      "created_at": 1699061776,
      "name": "Support FAQ",
      "bytes": 139920,
      "file_counts": {
        "in_progress": 0,
        "completed": 3,
        "failed": 0,
        "cancelled": 0,
        "total": 3
      }
    }

[

List vector stores

Beta


--------------------------

](/docs/api-reference/vector-stores/list)

get https://api.openai.com/v1/vector\_stores

Returns a list of vector stores.

### Query parameters

[](#vector-stores-list-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#vector-stores-list-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#vector-stores-list-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#vector-stores-list-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [vector store](/docs/api-reference/vector-stores/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/vector_stores \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    {
      "object": "list",
      "data": [
        {
          "id": "vs_abc123",
          "object": "vector_store",
          "created_at": 1699061776,
          "name": "Support FAQ",
          "bytes": 139920,
          "file_counts": {
            "in_progress": 0,
            "completed": 3,
            "failed": 0,
            "cancelled": 0,
            "total": 3
          }
        },
        {
          "id": "vs_abc456",
          "object": "vector_store",
          "created_at": 1699061776,
          "name": "Support FAQ v2",
          "bytes": 139920,
          "file_counts": {
            "in_progress": 0,
            "completed": 3,
            "failed": 0,
            "cancelled": 0,
            "total": 3
          }
        }
      ],
      "first_id": "vs_abc123",
      "last_id": "vs_abc456",
      "has_more": false
    }

[

Retrieve vector store

Beta


-----------------------------

](/docs/api-reference/vector-stores/retrieve)

get https://api.openai.com/v1/vector\_stores/{vector\_store\_id}

Retrieves a vector store.

### Path parameters

[](#vector-stores-retrieve-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store to retrieve.

### Returns

The [vector store](/docs/api-reference/vector-stores/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/vector_stores/vs_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    {
      "id": "vs_abc123",
      "object": "vector_store",
      "created_at": 1699061776
    }

[

Modify vector store

Beta


---------------------------

](/docs/api-reference/vector-stores/modify)

post https://api.openai.com/v1/vector\_stores/{vector\_store\_id}

Modifies a vector store.

### Path parameters

[](#vector-stores-modify-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store to modify.

### Request body

[](#vector-stores-modify-name)

name

string or null

Optional

The name of the vector store.

[](#vector-stores-modify-expires_after)

expires\_after

object

Optional

The expiration policy for a vector store.

Show properties

[](#vector-stores-modify-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [vector store](/docs/api-reference/vector-stores/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/vector_stores/vs_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"
      -d '{
        "name": "Support FAQ"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    {
      "id": "vs_abc123",
      "object": "vector_store",
      "created_at": 1699061776,
      "name": "Support FAQ",
      "bytes": 139920,
      "file_counts": {
        "in_progress": 0,
        "completed": 3,
        "failed": 0,
        "cancelled": 0,
        "total": 3
      }
    }

[

Delete vector store

Beta


---------------------------

](/docs/api-reference/vector-stores/delete)

delete https://api.openai.com/v1/vector\_stores/{vector\_store\_id}

Delete a vector store.

### Path parameters

[](#vector-stores-delete-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/vector_stores/vs_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      id: "vs_abc123",
      object: "vector_store.deleted",
      deleted: true
    }

[

The vector store object

Beta


-------------------------------

](/docs/api-reference/vector-stores/object)

A vector store is a collection of processed files can be used by the `file_search` tool.

[](#vector-stores/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#vector-stores/object-object)

object

string

The object type, which is always `vector_store`.

[](#vector-stores/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the vector store was created.

[](#vector-stores/object-name)

name

string

The name of the vector store.

[](#vector-stores/object-usage_bytes)

usage\_bytes

integer

The total number of bytes used by the files in the vector store.

[](#vector-stores/object-file_counts)

file\_counts

object

Show properties

[](#vector-stores/object-status)

status

string

The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

[](#vector-stores/object-expires_after)

expires\_after

object

The expiration policy for a vector store.

Show properties

[](#vector-stores/object-expires_at)

expires\_at

integer or null

The Unix timestamp (in seconds) for when the vector store will expire.

[](#vector-stores/object-last_active_at)

last\_active\_at

integer or null

The Unix timestamp (in seconds) for when the vector store was last active.

[](#vector-stores/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The vector store object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    {
      "id": "vs_123",
      "object": "vector_store",
      "created_at": 1698107661,
      "usage_bytes": 123456,
      "last_active_at": 1698107661,
      "name": "my_vector_store",
      "status": "completed",
      "file_counts": {
        "in_progress": 0,
        "completed": 100,
        "cancelled": 0,
        "failed": 0,
        "total": 100
      },
      "metadata": {},
      "last_used_at": 1698107661
    }

[

Vector Store Files

Beta


--------------------------

](/docs/api-reference/vector-stores-files)

Vector store files represent files inside a vector store.

Related guide: [File Search](/docs/assistants/tools/file-search)

[

Create vector store file

Beta


--------------------------------

](/docs/api-reference/vector-stores-files/createFile)

post https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/files

Create a vector store file by attaching a [File](/docs/api-reference/files) to a [vector store](/docs/api-reference/vector-stores/object).

### Path parameters

[](#vector-stores-files-createfile-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store for which to create a File.

### Request body

[](#vector-stores-files-createfile-file_id)

file\_id

string

Required

A [File](/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

[](#vector-stores-files-createfile-chunking_strategy)

chunking\_strategy

object

Optional

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

Show possible types

### Returns

A [vector store file](/docs/api-reference/vector-stores-files/file-object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "Content-Type: application/json" \
        -H "OpenAI-Beta: assistants=v2" \
        -d '{
          "file_id": "file-abc123"
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    {
      "id": "file-abc123",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "usage_bytes": 1234,
      "vector_store_id": "vs_abcd",
      "status": "completed",
      "last_error": null
    }

[

List vector store files

Beta


-------------------------------

](/docs/api-reference/vector-stores-files/listFiles)

get https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/files

Returns a list of vector store files.

### Path parameters

[](#vector-stores-files-listfiles-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store that the files belong to.

### Query parameters

[](#vector-stores-files-listfiles-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#vector-stores-files-listfiles-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#vector-stores-files-listfiles-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#vector-stores-files-listfiles-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

[](#vector-stores-files-listfiles-filter)

filter

string

Optional

Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

### Returns

A list of [vector store file](/docs/api-reference/vector-stores-files/file-object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "object": "list",
      "data": [
        {
          "id": "file-abc123",
          "object": "vector_store.file",
          "created_at": 1699061776,
          "vector_store_id": "vs_abc123"
        },
        {
          "id": "file-abc456",
          "object": "vector_store.file",
          "created_at": 1699061776,
          "vector_store_id": "vs_abc123"
        }
      ],
      "first_id": "file-abc123",
      "last_id": "file-abc456",
      "has_more": false
    }

[

Retrieve vector store file

Beta


----------------------------------

](/docs/api-reference/vector-stores-files/getFile)

get https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/files/{file\_id}

Retrieves a vector store file.

### Path parameters

[](#vector-stores-files-getfile-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store that the file belongs to.

[](#vector-stores-files-getfile-file_id)

file\_id

string

Required

The ID of the file being retrieved.

### Returns

The [vector store file](/docs/api-reference/vector-stores-files/file-object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    {
      "id": "file-abc123",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abcd",
      "status": "completed",
      "last_error": null
    }

[

Delete vector store file

Beta


--------------------------------

](/docs/api-reference/vector-stores-files/deleteFile)

delete https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/files/{file\_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](/docs/api-reference/files/delete) endpoint.

### Path parameters

[](#vector-stores-files-deletefile-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store that the file belongs to.

[](#vector-stores-files-deletefile-file_id)

file\_id

string

Required

The ID of the file to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      id: "file-abc123",
      object: "vector_store.file.deleted",
      deleted: true
    }

[

The vector store file object

Beta


------------------------------------

](/docs/api-reference/vector-stores-files/file-object)

A list of files attached to a vector store.

[](#vector-stores-files/file-object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#vector-stores-files/file-object-object)

object

string

The object type, which is always `vector_store.file`.

[](#vector-stores-files/file-object-usage_bytes)

usage\_bytes

integer

The total vector store usage in bytes. Note that this may be different from the original file size.

[](#vector-stores-files/file-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the vector store file was created.

[](#vector-stores-files/file-object-vector_store_id)

vector\_store\_id

string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

[](#vector-stores-files/file-object-status)

status

string

The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

[](#vector-stores-files/file-object-last_error)

last\_error

object or null

The last error associated with this vector store file. Will be `null` if there are no errors.

Show properties

[](#vector-stores-files/file-object-chunking_strategy)

chunking\_strategy

object

The strategy used to chunk the file.

Show possible types

The vector store file object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    {
      "id": "file-abc123",
      "object": "vector_store.file",
      "usage_bytes": 1234,
      "created_at": 1698107661,
      "vector_store_id": "vs_abc123",
      "status": "completed",
      "last_error": null,
      "chunking_strategy": {
        "type": "static",
        "static": {
          "max_chunk_size_tokens": 800,
          "chunk_overlap_tokens": 400
        }
      }
    }

[

Vector Store File Batches

Beta


---------------------------------

](/docs/api-reference/vector-stores-file-batches)

Vector store file batches represent operations to add multiple files to a vector store.

Related guide: [File Search](/docs/assistants/tools/file-search)

[

Create vector store file batch

Beta


--------------------------------------

](/docs/api-reference/vector-stores-file-batches/createBatch)

post https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/file\_batches

Create a vector store file batch.

### Path parameters

[](#vector-stores-file-batches-createbatch-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store for which to create a File Batch.

### Request body

[](#vector-stores-file-batches-createbatch-file_ids)

file\_ids

array

Required

A list of [File](/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

[](#vector-stores-file-batches-createbatch-chunking_strategy)

chunking\_strategy

object

Optional

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

Show possible types

### Returns

A [vector store file batch](/docs/api-reference/vector-stores-file-batches/batch-object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/vector_stores/vs_abc123/file_batches \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "Content-Type: application/json \
        -H "OpenAI-Beta: assistants=v2" \
        -d '{
          "file_ids": ["file-abc123", "file-abc456"]
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    {
      "id": "vsfb_abc123",
      "object": "vector_store.file_batch",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123",
      "status": "in_progress",
      "file_counts": {
        "in_progress": 1,
        "completed": 1,
        "failed": 0,
        "cancelled": 0,
        "total": 0,
      }
    }

[

Retrieve vector store file batch

Beta


----------------------------------------

](/docs/api-reference/vector-stores-file-batches/getBatch)

get https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}

Retrieves a vector store file batch.

### Path parameters

[](#vector-stores-file-batches-getbatch-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store that the file batch belongs to.

[](#vector-stores-file-batches-getbatch-batch_id)

batch\_id

string

Required

The ID of the file batch being retrieved.

### Returns

The [vector store file batch](/docs/api-reference/vector-stores-file-batches/batch-object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files_batches/vsfb_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    {
      "id": "vsfb_abc123",
      "object": "vector_store.file_batch",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123",
      "status": "in_progress",
      "file_counts": {
        "in_progress": 1,
        "completed": 1,
        "failed": 0,
        "cancelled": 0,
        "total": 0,
      }
    }

[

Cancel vector store file batch

Beta


--------------------------------------

](/docs/api-reference/vector-stores-file-batches/cancelBatch)

post https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/cancel

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

### Path parameters

[](#vector-stores-file-batches-cancelbatch-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store that the file batch belongs to.

[](#vector-stores-file-batches-cancelbatch-batch_id)

batch\_id

string

Required

The ID of the file batch to cancel.

### Returns

The modified vector store file batch object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files_batches/vsfb_abc123/cancel \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2" \
      -X POST

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    {
      "id": "vsfb_abc123",
      "object": "vector_store.file_batch",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123",
      "status": "cancelling",
      "file_counts": {
        "in_progress": 12,
        "completed": 3,
        "failed": 0,
        "cancelled": 0,
        "total": 15,
      }
    }

[

List vector store files in a batch

Beta


------------------------------------------

](/docs/api-reference/vector-stores-file-batches/listBatchFiles)

get https://api.openai.com/v1/vector\_stores/{vector\_store\_id}/file\_batches/{batch\_id}/files

Returns a list of vector store files in a batch.

### Path parameters

[](#vector-stores-file-batches-listbatchfiles-vector_store_id)

vector\_store\_id

string

Required

The ID of the vector store that the files belong to.

[](#vector-stores-file-batches-listbatchfiles-batch_id)

batch\_id

string

Required

The ID of the file batch that the files belong to.

### Query parameters

[](#vector-stores-file-batches-listbatchfiles-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#vector-stores-file-batches-listbatchfiles-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#vector-stores-file-batches-listbatchfiles-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#vector-stores-file-batches-listbatchfiles-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

[](#vector-stores-file-batches-listbatchfiles-filter)

filter

string

Optional

Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

### Returns

A list of [vector store file](/docs/api-reference/vector-stores-files/file-object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/vector_stores/vs_abc123/files_batches/vsfb_abc123/files \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v2"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "object": "list",
      "data": [
        {
          "id": "file-abc123",
          "object": "vector_store.file",
          "created_at": 1699061776,
          "vector_store_id": "vs_abc123"
        },
        {
          "id": "file-abc456",
          "object": "vector_store.file",
          "created_at": 1699061776,
          "vector_store_id": "vs_abc123"
        }
      ],
      "first_id": "file-abc123",
      "last_id": "file-abc456",
      "has_more": false
    }

[

The vector store files batch object

Beta


-------------------------------------------

](/docs/api-reference/vector-stores-file-batches/batch-object)

A batch of files attached to a vector store.

[](#vector-stores-file-batches/batch-object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#vector-stores-file-batches/batch-object-object)

object

string

The object type, which is always `vector_store.file_batch`.

[](#vector-stores-file-batches/batch-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the vector store files batch was created.

[](#vector-stores-file-batches/batch-object-vector_store_id)

vector\_store\_id

string

The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to.

[](#vector-stores-file-batches/batch-object-status)

status

string

The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

[](#vector-stores-file-batches/batch-object-file_counts)

file\_counts

object

Show properties

The vector store files batch object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    {
      "id": "vsfb_123",
      "object": "vector_store.files_batch",
      "created_at": 1698107661,
      "vector_store_id": "vs_abc123",
      "status": "completed",
      "file_counts": {
        "in_progress": 0,
        "completed": 100,
        "failed": 0,
        "cancelled": 0,
        "total": 100
      }
    }

[

Streaming

Beta


-----------------

](/docs/api-reference/assistants-streaming)

Stream the result of executing a Run or resuming a Run after submitting tool outputs.

You can stream events from the [Create Thread and Run](/docs/api-reference/runs/createThreadAndRun), [Create Run](/docs/api-reference/runs/createRun), and [Submit Tool Outputs](/docs/api-reference/runs/submitToolOutputs) endpoints by passing `"stream": true`. The response will be a [Server-Sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) stream.

Our Node and Python SDKs provide helpful utilities to make streaming easy. Reference the [Assistants API quickstart](/docs/assistants/overview) to learn more.

[

The message delta object

Beta


--------------------------------

](/docs/api-reference/assistants-streaming/message-delta-object)

Represents a message delta i.e. any changed fields on a message during streaming.

[](#assistants-streaming/message-delta-object-id)

id

string

The identifier of the message, which can be referenced in API endpoints.

[](#assistants-streaming/message-delta-object-object)

object

string

The object type, which is always `thread.message.delta`.

[](#assistants-streaming/message-delta-object-delta)

delta

object

The delta containing the fields that have changed on the Message.

Show properties

The message delta object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    {
      "id": "msg_123",
      "object": "thread.message.delta",
      "delta": {
        "content": [
          {
            "index": 0,
            "type": "text",
            "text": { "value": "Hello", "annotations": [] }
          }
        ]
      }
    }

[

The run step delta object

Beta


---------------------------------

](/docs/api-reference/assistants-streaming/run-step-delta-object)

Represents a run step delta i.e. any changed fields on a run step during streaming.

[](#assistants-streaming/run-step-delta-object-id)

id

string

The identifier of the run step, which can be referenced in API endpoints.

[](#assistants-streaming/run-step-delta-object-object)

object

string

The object type, which is always `thread.run.step.delta`.

[](#assistants-streaming/run-step-delta-object-delta)

delta

object

The delta containing the fields that have changed on the run step.

Show properties

The run step delta object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    {
      "id": "step_123",
      "object": "thread.run.step.delta",
      "delta": {
        "step_details": {
          "type": "tool_calls",
          "tool_calls": [
            {
              "index": 0,
              "id": "call_123",
              "type": "code_interpreter",
              "code_interpreter": { "input": "", "outputs": [] }
            }
          ]
        }
      }
    }

[

Assistant stream events

Beta


-------------------------------

](/docs/api-reference/assistants-streaming/events)

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

    event: thread.created
    data: {"id": "thread_123", "object": "thread", ...}

We emit events whenever a new object is created, transitions to a new state, or is being streamed in parts (deltas). For example, we emit `thread.run.created` when a new run is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses to create a message during a run, we emit a `thread.message.created event`, a `thread.message.in_progress` event, many `thread.message.delta` events, and finally a `thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully in your code. See the [Assistants API quickstart](/docs/assistants/overview) to learn how to integrate the Assistants API with streaming.

[](#assistants-streaming/events-thread-created)

thread.created

`data` is a [thread](/docs/api-reference/threads/object)

Occurs when a new [thread](/docs/api-reference/threads/object) is created.

[](#assistants-streaming/events-thread-run-created)

thread.run.created

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a new [run](/docs/api-reference/runs/object) is created.

[](#assistants-streaming/events-thread-run-queued)

thread.run.queued

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) moves to a `queued` status.

[](#assistants-streaming/events-thread-run-in_progress)

thread.run.in\_progress

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) moves to an `in_progress` status.

[](#assistants-streaming/events-thread-run-requires_action)

thread.run.requires\_action

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) moves to a `requires_action` status.

[](#assistants-streaming/events-thread-run-completed)

thread.run.completed

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) is completed.

[](#assistants-streaming/events-thread-run-incomplete)

thread.run.incomplete

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) ends with status `incomplete`.

[](#assistants-streaming/events-thread-run-failed)

thread.run.failed

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) fails.

[](#assistants-streaming/events-thread-run-cancelling)

thread.run.cancelling

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) moves to a `cancelling` status.

[](#assistants-streaming/events-thread-run-cancelled)

thread.run.cancelled

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) is cancelled.

[](#assistants-streaming/events-thread-run-expired)

thread.run.expired

`data` is a [run](/docs/api-reference/runs/object)

Occurs when a [run](/docs/api-reference/runs/object) expires.

[](#assistants-streaming/events-thread-run-step-created)

thread.run.step.created

`data` is a [run step](/docs/api-reference/runs/step-object)

Occurs when a [run step](/docs/api-reference/runs/step-object) is created.

[](#assistants-streaming/events-thread-run-step-in_progress)

thread.run.step.in\_progress

`data` is a [run step](/docs/api-reference/runs/step-object)

Occurs when a [run step](/docs/api-reference/runs/step-object) moves to an `in_progress` state.

[](#assistants-streaming/events-thread-run-step-delta)

thread.run.step.delta

`data` is a [run step delta](/docs/api-reference/assistants-streaming/run-step-delta-object)

Occurs when parts of a [run step](/docs/api-reference/runs/step-object) are being streamed.

[](#assistants-streaming/events-thread-run-step-completed)

thread.run.step.completed

`data` is a [run step](/docs/api-reference/runs/step-object)

Occurs when a [run step](/docs/api-reference/runs/step-object) is completed.

[](#assistants-streaming/events-thread-run-step-failed)

thread.run.step.failed

`data` is a [run step](/docs/api-reference/runs/step-object)

Occurs when a [run step](/docs/api-reference/runs/step-object) fails.

[](#assistants-streaming/events-thread-run-step-cancelled)

thread.run.step.cancelled

`data` is a [run step](/docs/api-reference/runs/step-object)

Occurs when a [run step](/docs/api-reference/runs/step-object) is cancelled.

[](#assistants-streaming/events-thread-run-step-expired)

thread.run.step.expired

`data` is a [run step](/docs/api-reference/runs/step-object)

Occurs when a [run step](/docs/api-reference/runs/step-object) expires.

[](#assistants-streaming/events-thread-message-created)

thread.message.created

`data` is a [message](/docs/api-reference/messages/object)

Occurs when a [message](/docs/api-reference/messages/object) is created.

[](#assistants-streaming/events-thread-message-in_progress)

thread.message.in\_progress

`data` is a [message](/docs/api-reference/messages/object)

Occurs when a [message](/docs/api-reference/messages/object) moves to an `in_progress` state.

[](#assistants-streaming/events-thread-message-delta)

thread.message.delta

`data` is a [message delta](/docs/api-reference/assistants-streaming/message-delta-object)

Occurs when parts of a [Message](/docs/api-reference/messages/object) are being streamed.

[](#assistants-streaming/events-thread-message-completed)

thread.message.completed

`data` is a [message](/docs/api-reference/messages/object)

Occurs when a [message](/docs/api-reference/messages/object) is completed.

[](#assistants-streaming/events-thread-message-incomplete)

thread.message.incomplete

`data` is a [message](/docs/api-reference/messages/object)

Occurs when a [message](/docs/api-reference/messages/object) ends before it is completed.

[](#assistants-streaming/events-error)

error

`data` is an [error](/docs/guides/error-codes/api-errors)

Occurs when an [error](/docs/guides/error-codes/api-errors) occurs. This can happen due to an internal server error or a timeout.

[](#assistants-streaming/events-done)

done

`data` is `[DONE]`

Occurs when a stream ends.

[

Completions

Legacy


---------------------

](/docs/api-reference/completions)

Given a prompt, the model will return one or more predicted completions along with the probabilities of alternative tokens at each position. Most developer should use our [Chat Completions API](/docs/guides/text-generation/text-generation-models) to leverage our best and newest models.

[

Create completion

Legacy


---------------------------

](/docs/api-reference/completions/create)

post https://api.openai.com/v1/completions

Creates a completion for the provided prompt and parameters.

### Request body

[](#completions-create-model)

model

string

Required

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

[](#completions-create-prompt)

prompt

string or array

Required

The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.

Note that <|end-of-text|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.

[](#completions-create-best_of)

best\_of

integer or null

Optional

Defaults to 1

Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.

When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

[](#completions-create-echo)

echo

boolean or null

Optional

Defaults to false

Echo back the prompt in addition to the completion

[](#completions-create-frequency_penalty)

frequency\_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)

[](#completions-create-logit_bias)

logit\_bias

map

Optional

Defaults to null

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

As an example, you can pass `{"50256": -100}` to prevent the <|end-of-text|> token from being generated.

[](#completions-create-logprobs)

logprobs

integer or null

Optional

Defaults to null

Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.

The maximum value for `logprobs` is 5.

[](#completions-create-max_tokens)

max\_tokens

integer or null

Optional

Defaults to 16

The maximum number of [tokens](/tokenizer) that can be generated in the completion.

The token count of your prompt plus `max_tokens` cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

[](#completions-create-n)

n

integer or null

Optional

Defaults to 1

How many completions to generate for each prompt.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

[](#completions-create-presence_penalty)

presence\_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

[See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)

[](#completions-create-seed)

seed

integer or null

Optional

If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.

Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

[](#completions-create-stop)

stop

string / array / null

Optional

Defaults to null

Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.

[](#completions-create-stream)

stream

boolean or null

Optional

Defaults to false

Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

[](#completions-create-stream_options)

stream\_options

object or null

Optional

Defaults to null

Options for streaming response. Only set this when you set `stream: true`.

Show properties

[](#completions-create-suffix)

suffix

string or null

Optional

Defaults to null

The suffix that comes after a completion of inserted text.

This parameter is only supported for `gpt-3.5-turbo-instruct`.

[](#completions-create-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or `top_p` but not both.

[](#completions-create-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or `temperature` but not both.

[](#completions-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a [completion](/docs/api-reference/completions/object) object, or a sequence of completion objects if the request is streamed.

No streaming‍Streaming‍

Example request

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    curl https://api.openai.com/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "gpt-3.5-turbo-instruct",
        "prompt": "Say this is a test",
        "max_tokens": 7,
        "temperature": 0
      }'

Response

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
      "object": "text_completion",
      "created": 1589478378,
      "model": "gpt-3.5-turbo-instruct",
      "system_fingerprint": "fp_44709d6fcb",
      "choices": [
        {
          "text": "\n\nThis is indeed a test",
          "index": 0,
          "logprobs": null,
          "finish_reason": "length"
        }
      ],
      "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 7,
        "total_tokens": 12
      }
    }

[

The completion object

Legacy


-------------------------------

](/docs/api-reference/completions/object)

Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).

[](#completions/object-id)

id

string

A unique identifier for the completion.

[](#completions/object-choices)

choices

array

The list of completion choices the model generated for the input prompt.

Show properties

[](#completions/object-created)

created

integer

The Unix timestamp (in seconds) of when the completion was created.

[](#completions/object-model)

model

string

The model used for completion.

[](#completions/object-system_fingerprint)

system\_fingerprint

string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](#completions/object-object)

object

string

The object type, which is always "text\_completion"

[](#completions/object-usage)

usage

object

Usage statistics for the completion request.

Show properties

The completion object

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    {
      "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
      "object": "text_completion",
      "created": 1589478378,
      "model": "gpt-4-turbo",
      "choices": [
        {
          "text": "\n\nThis is indeed a test",
          "index": 0,
          "logprobs": null,
          "finish_reason": "length"
        }
      ],
      "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 7,
        "total_tokens": 12
      }
    }

[

Assistants (v1)

Legacy


-------------------------

](/docs/api-reference/assistants-v1)

Build assistants that can call models and use tools to perform tasks.

[Get started with the Assistants API](/docs/assistants)

[

Create assistant (v1)

Legacy


-------------------------------

](/docs/api-reference/assistants-v1/createAssistant)

post https://api.openai.com/v1/assistants

Create an assistant with a model and instructions.

### Request body

[](#assistants-v1-createassistant-model)

model

string

Required

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them. type: string

[](#assistants-v1-createassistant-name)

name

string or null

Optional

The name of the assistant. The maximum length is 256 characters.

[](#assistants-v1-createassistant-description)

description

string or null

Optional

The description of the assistant. The maximum length is 512 characters.

[](#assistants-v1-createassistant-instructions)

instructions

string or null

Optional

The system instructions that the assistant uses. The maximum length is 256,000 characters.

[](#assistants-v1-createassistant-tools)

tools

array

Optional

Defaults to \[\]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

Show possible types

[](#assistants-v1-createassistant-file_ids)

file\_ids

array

Optional

Defaults to \[\]

A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.

[](#assistants-v1-createassistant-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#assistants-v1-createassistant-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#assistants-v1-createassistant-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#assistants-v1-createassistant-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

An [assistant](/docs/api-reference/assistants-v1/object) object.

Code Interpreter‍Files‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl "https://api.openai.com/v1/assistants" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
        "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        "name": "Math Tutor",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-turbo"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1698984975,
      "name": "Math Tutor",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [],
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

Create assistant file (v1)

Legacy


------------------------------------

](/docs/api-reference/assistants-v1/createAssistantFile)

post https://api.openai.com/v1/assistants/{assistant\_id}/files

Create an assistant file by attaching a [File](/docs/api-reference/files) to an [assistant](/docs/api-reference/assistants-v1).

### Path parameters

[](#assistants-v1-createassistantfile-assistant_id)

assistant\_id

string

Required

The ID of the assistant for which to create a File.

### Request body

[](#assistants-v1-createassistantfile-file_id)

file\_id

string

Required

A [File](/docs/api-reference/files) ID (with `purpose="assistants"`) that the assistant should use. Useful for tools like `retrieval` and `code_interpreter` that can access files.

### Returns

An [assistant file](/docs/api-reference/assistants-v1/file-object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/assistants/asst_abc123/files \
        -H 'Authorization: Bearer $OPENAI_API_KEY"' \
        -H 'Content-Type: application/json' \
        -H 'OpenAI-Beta: assistants=v1' \
        -d '{
          "file_id": "file-abc123"
        }'

Response

    1
    2
    3
    4
    5
    6
    {
      "id": "file-abc123",
      "object": "assistant.file",
      "created_at": 1699055364,
      "assistant_id": "asst_abc123"
    }

[

List assistants (v1)

Legacy


------------------------------

](/docs/api-reference/assistants-v1/listAssistants)

get https://api.openai.com/v1/assistants

Returns a list of assistants.

### Query parameters

[](#assistants-v1-listassistants-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#assistants-v1-listassistants-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#assistants-v1-listassistants-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#assistants-v1-listassistants-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [assistant](/docs/api-reference/assistants-v1/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl "https://api.openai.com/v1/assistants?order=desc&limit=20" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    {
      "object": "list",
      "data": [
        {
          "id": "asst_abc123",
          "object": "assistant",
          "created_at": 1698982736,
          "name": "Coding Tutor",
          "description": null,
          "model": "gpt-4-turbo",
          "instructions": "You are a helpful assistant designed to make me better at coding!",
          "tools": [],
          "file_ids": [],
          "metadata": {},
          "top_p": 1.0,
          "temperature": 1.0,
          "response_format": "auto"
        },
        {
          "id": "asst_abc456",
          "object": "assistant",
          "created_at": 1698982718,
          "name": "My Assistant",
          "description": null,
          "model": "gpt-4-turbo",
          "instructions": "You are a helpful assistant designed to make me better at coding!",
          "tools": [],
          "file_ids": [],
          "metadata": {},
          "top_p": 1.0,
          "temperature": 1.0,
          "response_format": "auto"
        },
        {
          "id": "asst_abc789",
          "object": "assistant",
          "created_at": 1698982643,
          "name": null,
          "description": null,
          "model": "gpt-4-turbo",
          "instructions": null,
          "tools": [],
          "file_ids": [],
          "metadata": {},
          "top_p": 1.0,
          "temperature": 1.0,
          "response_format": "auto"
        }
      ],
      "first_id": "asst_abc123",
      "last_id": "asst_abc789",
      "has_more": false
    }

[

List assistant files (v1)

Legacy


-----------------------------------

](/docs/api-reference/assistants-v1/listAssistantFiles)

get https://api.openai.com/v1/assistants/{assistant\_id}/files

Returns a list of assistant files.

### Path parameters

[](#assistants-v1-listassistantfiles-assistant_id)

assistant\_id

string

Required

The ID of the assistant the file belongs to.

### Query parameters

[](#assistants-v1-listassistantfiles-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#assistants-v1-listassistantfiles-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#assistants-v1-listassistantfiles-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#assistants-v1-listassistantfiles-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [assistant file](/docs/api-reference/assistants-v1/file-object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/assistants/asst_abc123/files \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "object": "list",
      "data": [
        {
          "id": "file-abc123",
          "object": "assistant.file",
          "created_at": 1699060412,
          "assistant_id": "asst_abc123"
        },
        {
          "id": "file-abc456",
          "object": "assistant.file",
          "created_at": 1699060412,
          "assistant_id": "asst_abc123"
        }
      ],
      "first_id": "file-abc123",
      "last_id": "file-abc456",
      "has_more": false
    }

[

Retrieve assistant (v1)

Legacy


---------------------------------

](/docs/api-reference/assistants-v1/getAssistant)

get https://api.openai.com/v1/assistants/{assistant\_id}

Retrieves an assistant.

### Path parameters

[](#assistants-v1-getassistant-assistant_id)

assistant\_id

string

Required

The ID of the assistant to retrieve.

### Returns

The [assistant](/docs/api-reference/assistants-v1/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/assistants/asst_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1699009709,
      "name": "HR Helper",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies.",
      "tools": [
        {
          "type": "retrieval"
        }
      ],
      "file_ids": [
        "file-abc123"
      ],
      "metadata": {}
    }

[

Retrieve assistant file (v1)

Legacy


--------------------------------------

](/docs/api-reference/assistants-v1/getAssistantFile)

get https://api.openai.com/v1/assistants/{assistant\_id}/files/{file\_id}

Retrieves an AssistantFile.

### Path parameters

[](#assistants-v1-getassistantfile-assistant_id)

assistant\_id

string

Required

The ID of the assistant who the file belongs to.

[](#assistants-v1-getassistantfile-file_id)

file\_id

string

Required

The ID of the file we're getting.

### Returns

The [assistant file](/docs/api-reference/assistants-v1/file-object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/assistants/asst_abc123/files/file-abc123 \
      -H 'Authorization: Bearer $OPENAI_API_KEY"' \
      -H 'Content-Type: application/json' \
      -H 'OpenAI-Beta: assistants=v1'

Response

    1
    2
    3
    4
    5
    6
    {
      "id": "file-abc123",
      "object": "assistant.file",
      "created_at": 1699055364,
      "assistant_id": "asst_abc123"
    }

[

Modify assistant (v1)

Legacy


-------------------------------

](/docs/api-reference/assistants-v1/modifyAssistant)

post https://api.openai.com/v1/assistants/{assistant\_id}

Modifies an assistant.

### Path parameters

[](#assistants-v1-modifyassistant-assistant_id)

assistant\_id

string

Required

The ID of the assistant to modify.

### Request body

[](#assistants-v1-modifyassistant-model)

model

Optional

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them. type: string

[](#assistants-v1-modifyassistant-name)

name

string or null

Optional

The name of the assistant. The maximum length is 256 characters.

[](#assistants-v1-modifyassistant-description)

description

string or null

Optional

The description of the assistant. The maximum length is 512 characters.

[](#assistants-v1-modifyassistant-instructions)

instructions

string or null

Optional

The system instructions that the assistant uses. The maximum length is 256,000 characters.

[](#assistants-v1-modifyassistant-tools)

tools

array

Optional

Defaults to \[\]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

Show possible types

[](#assistants-v1-modifyassistant-file_ids)

file\_ids

array

Optional

Defaults to \[\]

A list of [File](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order. If a file was previously attached to the list but does not show up in the list, it will be deleted from the assistant.

[](#assistants-v1-modifyassistant-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#assistants-v1-modifyassistant-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#assistants-v1-modifyassistant-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#assistants-v1-modifyassistant-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

The modified [assistant](/docs/api-reference/assistants-v1/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl https://api.openai.com/v1/assistants/asst_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
          "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
          "tools": [{"type": "retrieval"}],
          "model": "gpt-4-turbo",
          "file_ids": ["file-abc123", "file-abc456"]
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1699009709,
      "name": "HR Helper",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
      "tools": [
        {
          "type": "retrieval"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

Delete assistant (v1)

Legacy


-------------------------------

](/docs/api-reference/assistants-v1/deleteAssistant)

delete https://api.openai.com/v1/assistants/{assistant\_id}

Delete an assistant.

### Path parameters

[](#assistants-v1-deleteassistant-assistant_id)

assistant\_id

string

Required

The ID of the assistant to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/assistants/asst_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      "id": "asst_abc123",
      "object": "assistant.deleted",
      "deleted": true
    }

[

Delete assistant file (v1)

Legacy


------------------------------------

](/docs/api-reference/assistants-v1/deleteAssistantFile)

delete https://api.openai.com/v1/assistants/{assistant\_id}/files/{file\_id}

Delete an assistant file.

### Path parameters

[](#assistants-v1-deleteassistantfile-assistant_id)

assistant\_id

string

Required

The ID of the assistant that the file belongs to.

[](#assistants-v1-deleteassistantfile-file_id)

file\_id

string

Required

The ID of the file to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/assistants/asst_abc123/files/file-abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      id: "file-abc123",
      object: "assistant.file.deleted",
      deleted: true
    }

[

The assistant object (v1)

Legacy


-----------------------------------

](/docs/api-reference/assistants-v1/object)

Represents an `assistant` that can call the model and use tools.

[](#assistants-v1/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#assistants-v1/object-object)

object

string

The object type, which is always `assistant`.

[](#assistants-v1/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the assistant was created.

[](#assistants-v1/object-name)

name

string or null

The name of the assistant. The maximum length is 256 characters.

[](#assistants-v1/object-description)

description

string or null

The description of the assistant. The maximum length is 512 characters.

[](#assistants-v1/object-model)

model

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them. type: string

[](#assistants-v1/object-instructions)

instructions

string or null

The system instructions that the assistant uses. The maximum length is 256,000 characters.

[](#assistants-v1/object-tools)

tools

array

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

Show possible types

[](#assistants-v1/object-file_ids)

file\_ids

array

A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.

[](#assistants-v1/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#assistants-v1/object-temperature)

temperature

number or null

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#assistants-v1/object-top_p)

top\_p

number or null

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#assistants-v1/object-response_format)

response\_format

string or object

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

The assistant object (v1)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1698984975,
      "name": "Math Tutor",
      "description": null,
      "model": "gpt-4-turbo",
      "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [],
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }

[

The assistant file object (v1)

Legacy


----------------------------------------

](/docs/api-reference/assistants-v1/file-object)

A list of [Files](/docs/api-reference/files) attached to an `assistant`.

[](#assistants-v1/file-object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#assistants-v1/file-object-object)

object

string

The object type, which is always `assistant.file`.

[](#assistants-v1/file-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the assistant file was created.

[](#assistants-v1/file-object-assistant_id)

assistant\_id

string

The assistant ID that the file is attached to.

The assistant file object (v1)

    1
    2
    3
    4
    5
    6
    {
      "id": "file-abc123",
      "object": "assistant.file",
      "created_at": 1699055364,
      "assistant_id": "asst_abc123"
    }

[

Threads (v1)

Legacy


----------------------

](/docs/api-reference/threads-v1)

Create threads that assistants can interact with.

Related guide: [Assistants](/docs/assistants/overview)

[

Create thread (v1)

Legacy


----------------------------

](/docs/api-reference/threads-v1/createThread)

post https://api.openai.com/v1/threads

Create a thread.

### Request body

[](#threads-v1-createthread-messages)

messages

array

Optional

A list of [messages](/docs/api-reference/messages-v1) to start the thread with.

Show properties

[](#threads-v1-createthread-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [thread](/docs/api-reference/threads-v1) object.

Empty‍Messages‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/threads \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -d ''

Response

    1
    2
    3
    4
    5
    6
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1699012949,
      "metadata": {}
    }

[

Retrieve thread (v1)

Legacy


------------------------------

](/docs/api-reference/threads-v1/getThread)

get https://api.openai.com/v1/threads/{thread\_id}

Retrieves a thread.

### Path parameters

[](#threads-v1-getthread-thread_id)

thread\_id

string

Required

The ID of the thread to retrieve.

### Returns

The [thread](/docs/api-reference/threads-v1/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1699014083,
      "metadata": {}
    }

[

Modify thread (v1)

Legacy


----------------------------

](/docs/api-reference/threads-v1/modifyThread)

post https://api.openai.com/v1/threads/{thread\_id}

Modifies a thread.

### Path parameters

[](#threads-v1-modifythread-thread_id)

thread\_id

string

Required

The ID of the thread to modify. Only the `metadata` can be modified.

### Request body

[](#threads-v1-modifythread-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [thread](/docs/api-reference/threads-v1/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl https://api.openai.com/v1/threads/thread_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
          "metadata": {
            "modified": "true",
            "user": "abc123"
          }
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1699014083,
      "metadata": {
        "modified": "true",
        "user": "abc123"
      }
    }

[

Delete thread (v1)

Legacy


----------------------------

](/docs/api-reference/threads-v1/deleteThread)

delete https://api.openai.com/v1/threads/{thread\_id}

Delete a thread.

### Path parameters

[](#threads-v1-deletethread-thread_id)

thread\_id

string

Required

The ID of the thread to delete.

### Returns

Deletion status

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    curl https://api.openai.com/v1/threads/thread_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -X DELETE

Response

    1
    2
    3
    4
    5
    {
      "id": "thread_abc123",
      "object": "thread.deleted",
      "deleted": true
    }

[

The thread object (v1)

Legacy


--------------------------------

](/docs/api-reference/threads-v1/object)

Represents a thread that contains [messages](/docs/api-reference/messages-v1).

[](#threads-v1/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#threads-v1/object-object)

object

string

The object type, which is always `thread`.

[](#threads-v1/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the thread was created.

[](#threads-v1/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The thread object (v1)

    1
    2
    3
    4
    5
    6
    {
      "id": "thread_abc123",
      "object": "thread",
      "created_at": 1698107661,
      "metadata": {}
    }

[

Messages (v1)

Legacy


-----------------------

](/docs/api-reference/messages-v1)

Create messages within threads

Related guide: [Assistants](/docs/assistants/overview)

[

Create message (v1)

Legacy


-----------------------------

](/docs/api-reference/messages-v1/createMessage)

post https://api.openai.com/v1/threads/{thread\_id}/messages

Create a message.

### Path parameters

[](#messages-v1-createmessage-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads-v1) to create a message for.

### Request body

[](#messages-v1-createmessage-role)

role

string

Required

The role of the entity that is creating the message. Allowed values include:

*   `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
*   `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

[](#messages-v1-createmessage-content)

content

string

Required

The content of the message.

[](#messages-v1-createmessage-file_ids)

file\_ids

array

Optional

Defaults to \[\]

A list of [File](/docs/api-reference/files) IDs that the message should use. There can be a maximum of 10 files attached to a message. Useful for tools like `retrieval` and `code_interpreter` that can access and use files.

[](#messages-v1-createmessage-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [message](/docs/api-reference/messages-v1/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    curl https://api.openai.com/v1/threads/thread_abc123/messages \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
          "role": "user",
          "content": "How does AI work? Explain it in simple terms."
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699017614,
      "thread_id": "thread_abc123",
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "file_ids": [],
      "assistant_id": null,
      "run_id": null,
      "metadata": {}
    }

[

List messages (v1)

Legacy


----------------------------

](/docs/api-reference/messages-v1/listMessages)

get https://api.openai.com/v1/threads/{thread\_id}/messages

Returns a list of messages for a given thread.

### Path parameters

[](#messages-v1-listmessages-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads-v1) the messages belong to.

### Query parameters

[](#messages-v1-listmessages-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#messages-v1-listmessages-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#messages-v1-listmessages-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#messages-v1-listmessages-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

[](#messages-v1-listmessages-run_id)

run\_id

string

Optional

Filter messages by the run ID that generated them.

### Returns

A list of [message](/docs/api-reference/messages-v1) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/messages \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    {
      "object": "list",
      "data": [
        {
          "id": "msg_abc123",
          "object": "thread.message",
          "created_at": 1699016383,
          "thread_id": "thread_abc123",
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": {
                "value": "How does AI work? Explain it in simple terms.",
                "annotations": []
              }
            }
          ],
          "file_ids": [],
          "assistant_id": null,
          "run_id": null,
          "metadata": {}
        },
        {
          "id": "msg_abc456",
          "object": "thread.message",
          "created_at": 1699016383,
          "thread_id": "thread_abc123",
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": {
                "value": "Hello, what is AI?",
                "annotations": []
              }
            }
          ],
          "file_ids": [
            "file-abc123"
          ],
          "assistant_id": null,
          "run_id": null,
          "metadata": {}
        }
      ],
      "first_id": "msg_abc123",
      "last_id": "msg_abc456",
      "has_more": false
    }

[

List message files (v1)

Legacy


---------------------------------

](/docs/api-reference/messages-v1/listMessageFiles)

get https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}/files

Returns a list of message files.

### Path parameters

[](#messages-v1-listmessagefiles-thread_id)

thread\_id

string

Required

The ID of the thread that the message and files belong to.

[](#messages-v1-listmessagefiles-message_id)

message\_id

string

Required

The ID of the message that the files belongs to.

### Query parameters

[](#messages-v1-listmessagefiles-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#messages-v1-listmessagefiles-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#messages-v1-listmessagefiles-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#messages-v1-listmessagefiles-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [message file](/docs/api-reference/messages-v1/file-object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123/files \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "object": "list",
      "data": [
        {
          "id": "file-abc123",
          "object": "thread.message.file",
          "created_at": 1699061776,
          "message_id": "msg_abc123"
        },
        {
          "id": "file-abc123",
          "object": "thread.message.file",
          "created_at": 1699061776,
          "message_id": "msg_abc123"
        }
      ],
      "first_id": "file-abc123",
      "last_id": "file-abc123",
      "has_more": false
    }

[

Retrieve message (v1)

Legacy


-------------------------------

](/docs/api-reference/messages-v1/getMessage)

get https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}

Retrieve a message.

### Path parameters

[](#messages-v1-getmessage-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads-v1) to which this message belongs.

[](#messages-v1-getmessage-message_id)

message\_id

string

Required

The ID of the message to retrieve.

### Returns

The [message](/docs/api-reference/threads-v1/messages/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699017614,
      "thread_id": "thread_abc123",
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "file_ids": [],
      "assistant_id": null,
      "run_id": null,
      "metadata": {}
    }

[

Retrieve message file (v1)

Legacy


------------------------------------

](/docs/api-reference/messages-v1/getMessageFile)

get https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}/files/{file\_id}

Retrieves a message file.

### Path parameters

[](#messages-v1-getmessagefile-thread_id)

thread\_id

string

Required

The ID of the thread to which the message and File belong.

[](#messages-v1-getmessagefile-message_id)

message\_id

string

Required

The ID of the message the file belongs to.

[](#messages-v1-getmessagefile-file_id)

file\_id

string

Required

The ID of the file being retrieved.

### Returns

The [message file](/docs/api-reference/messages-v1/file-object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123/files/file-abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    {
      "id": "file-abc123",
      "object": "thread.message.file",
      "created_at": 1699061776,
      "message_id": "msg_abc123"
    }

[

Modify message (v1)

Legacy


-----------------------------

](/docs/api-reference/messages-v1/modifyMessage)

post https://api.openai.com/v1/threads/{thread\_id}/messages/{message\_id}

Modifies a message.

### Path parameters

[](#messages-v1-modifymessage-thread_id)

thread\_id

string

Required

The ID of the thread to which this message belongs.

[](#messages-v1-modifymessage-message_id)

message\_id

string

Required

The ID of the message to modify.

### Request body

[](#messages-v1-modifymessage-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [message](/docs/api-reference/threads-v1/messages/object) object.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    curl https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
          "metadata": {
            "modified": "true",
            "user": "abc123"
          }
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699017614,
      "thread_id": "thread_abc123",
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "file_ids": [],
      "assistant_id": null,
      "run_id": null,
      "metadata": {
        "modified": "true",
        "user": "abc123"
      }
    }

[

The message object (v1)

Legacy


---------------------------------

](/docs/api-reference/messages-v1/object)

Represents a message within a [thread](/docs/api-reference/threads-v1).

[](#messages-v1/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#messages-v1/object-object)

object

string

The object type, which is always `thread.message`.

[](#messages-v1/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the message was created.

[](#messages-v1/object-thread_id)

thread\_id

string

The [thread](/docs/api-reference/threads-v1) ID that this message belongs to.

[](#messages-v1/object-status)

status

string

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

[](#messages-v1/object-incomplete_details)

incomplete\_details

object or null

On an incomplete message, details about why the message is incomplete.

Show properties

[](#messages-v1/object-completed_at)

completed\_at

integer or null

The Unix timestamp (in seconds) for when the message was completed.

[](#messages-v1/object-incomplete_at)

incomplete\_at

integer or null

The Unix timestamp (in seconds) for when the message was marked as incomplete.

[](#messages-v1/object-role)

role

string

The entity that produced the message. One of `user` or `assistant`.

[](#messages-v1/object-content)

content

array

The content of the message in array of text and/or images.

Show possible types

[](#messages-v1/object-assistant_id)

assistant\_id

string or null

If applicable, the ID of the [assistant](/docs/api-reference/assistants-v1) that authored this message.

[](#messages-v1/object-run_id)

run\_id

string or null

The ID of the [run](/docs/api-reference/runs-v1) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

[](#messages-v1/object-file_ids)

file\_ids

array

A list of [file](/docs/api-reference/files) IDs that the assistant should use. Useful for tools like retrieval and code\_interpreter that can access files. A maximum of 10 files can be attached to a message.

[](#messages-v1/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The message object (v1)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1698983503,
      "thread_id": "thread_abc123",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "Hi! How can I help you today?",
            "annotations": []
          }
        }
      ],
      "file_ids": [],
      "assistant_id": "asst_abc123",
      "run_id": "run_abc123",
      "metadata": {}
    }

[

The message file object (v1)

Legacy


--------------------------------------

](/docs/api-reference/messages-v1/file-object)

A list of files attached to a `message`.

[](#messages-v1/file-object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#messages-v1/file-object-object)

object

string

The object type, which is always `thread.message.file`.

[](#messages-v1/file-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the message file was created.

[](#messages-v1/file-object-message_id)

message\_id

string

The ID of the [message](/docs/api-reference/messages-v1) that the [File](/docs/api-reference/files) is attached to.

The message file object (v1)

    1
    2
    3
    4
    5
    6
    7
    {
      "id": "file-abc123",
      "object": "thread.message.file",
      "created_at": 1698107661,
      "message_id": "message_QLoItBbqwyAJEzlTy4y9kOMM",
      "file_id": "file-abc123"
    }

[

Runs (v1)

Legacy


-------------------

](/docs/api-reference/runs-v1)

Represents an execution run on a thread.

Related guide: [Assistants](/docs/assistants/overview)

[

Create run (v1)

Legacy


-------------------------

](/docs/api-reference/runs-v1/createRun)

post https://api.openai.com/v1/threads/{thread\_id}/runs

Create a run.

### Path parameters

[](#runs-v1-createrun-thread_id)

thread\_id

string

Required

The ID of the thread to run.

### Request body

[](#runs-v1-createrun-assistant_id)

assistant\_id

string

Required

The ID of the [assistant](/docs/api-reference/assistants-v1) to use to execute this run.

[](#runs-v1-createrun-model)

model

string

Optional

The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

[](#runs-v1-createrun-instructions)

instructions

string or null

Optional

Overrides the [instructions](/docs/api-reference/assistants-v1/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

[](#runs-v1-createrun-additional_instructions)

additional\_instructions

string or null

Optional

Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

[](#runs-v1-createrun-additional_messages)

additional\_messages

array or null

Optional

Adds additional messages to the thread before creating the run.

Show properties

[](#runs-v1-createrun-tools)

tools

array or null

Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

Show possible types

[](#runs-v1-createrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs-v1-createrun-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#runs-v1-createrun-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#runs-v1-createrun-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

[](#runs-v1-createrun-max_prompt_tokens)

max\_prompt\_tokens

integer or null

Optional

The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

[](#runs-v1-createrun-max_completion_tokens)

max\_completion\_tokens

integer or null

Optional

The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

[](#runs-v1-createrun-truncation_strategy)

truncation\_strategy

object

Optional

Show properties

[](#runs-v1-createrun-tool_choice)

tool\_choice

string or object

Optional

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling a tool. Specifying a particular tool like `{"type": "TOOL_TYPE"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Show possible types

[](#runs-v1-createrun-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

A [run](/docs/api-reference/runs-v1/object) object.

Default‍Streaming‍Streaming with Functions‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/threads/thread_abc123/runs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
        "assistant_id": "asst_abc123"
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699063290,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "queued",
      "started_at": 1699063290,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699063291,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "usage": null,
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    }

[

Create thread and run (v1)

Legacy


------------------------------------

](/docs/api-reference/runs-v1/createThreadAndRun)

post https://api.openai.com/v1/threads/runs

Create a thread and run it in one request.

### Request body

[](#runs-v1-createthreadandrun-assistant_id)

assistant\_id

string

Required

The ID of the [assistant](/docs/api-reference/assistants-v1) to use to execute this run.

[](#runs-v1-createthreadandrun-thread)

thread

object

Optional

Show properties

[](#runs-v1-createthreadandrun-model)

model

string

Optional

The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

[](#runs-v1-createthreadandrun-instructions)

instructions

string or null

Optional

Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

[](#runs-v1-createthreadandrun-tools)

tools

array or null

Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

[](#runs-v1-createthreadandrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs-v1-createthreadandrun-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](#runs-v1-createthreadandrun-top_p)

top\_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

[](#runs-v1-createthreadandrun-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

[](#runs-v1-createthreadandrun-max_prompt_tokens)

max\_prompt\_tokens

integer or null

Optional

The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

[](#runs-v1-createthreadandrun-max_completion_tokens)

max\_completion\_tokens

integer or null

Optional

The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

[](#runs-v1-createthreadandrun-truncation_strategy)

truncation\_strategy

object

Optional

Show properties

[](#runs-v1-createthreadandrun-tool_choice)

tool\_choice

string or object

Optional

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling a tool. Specifying a particular tool like `{"type": "TOOL_TYPE"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Show possible types

[](#runs-v1-createthreadandrun-response_format)

response\_format

string or object

Optional

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

### Returns

A [run](/docs/api-reference/runs-v1/object) object.

Default‍Streaming‍Streaming with Functions‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    curl https://api.openai.com/v1/threads/runs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
          "assistant_id": "asst_abc123",
          "thread": {
            "messages": [
              {"role": "user", "content": "Explain deep learning to a 5 year old."}
            ]
          }
        }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699076792,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "queued",
      "started_at": null,
      "expires_at": 1699077392,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": null,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": "You are a helpful assistant.",
      "tools": [],
      "file_ids": [],
      "metadata": {},
      "usage": null,
      "temperature": 1
    }

[

List runs (v1)

Legacy


------------------------

](/docs/api-reference/runs-v1/listRuns)

get https://api.openai.com/v1/threads/{thread\_id}/runs

Returns a list of runs belonging to a thread.

### Path parameters

[](#runs-v1-listruns-thread_id)

thread\_id

string

Required

The ID of the thread the run belongs to.

### Query parameters

[](#runs-v1-listruns-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#runs-v1-listruns-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#runs-v1-listruns-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#runs-v1-listruns-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [run](/docs/api-reference/runs-v1/object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74
    75
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87
    88
    89
    90
    91
    92
    {
      "object": "list",
      "data": [
        {
          "id": "run_abc123",
          "object": "thread.run",
          "created_at": 1699075072,
          "assistant_id": "asst_abc123",
          "thread_id": "thread_abc123",
          "status": "completed",
          "started_at": 1699075072,
          "expires_at": null,
          "cancelled_at": null,
          "failed_at": null,
          "completed_at": 1699075073,
          "last_error": null,
          "model": "gpt-4-turbo",
          "instructions": null,
          "incomplete_details": null,
          "tools": [
            {
              "type": "code_interpreter"
            }
          ],
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ],
          "metadata": {},
          "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 456,
            "total_tokens": 579
          },
          "temperature": 1.0,
          "top_p": 1.0,
          "max_prompt_tokens": 1000,
          "max_completion_tokens": 1000,
          "truncation_strategy": {
            "type": "auto",
            "last_messages": null
          },
          "response_format": "auto",
          "tool_choice": "auto"
        },
        {
          "id": "run_abc456",
          "object": "thread.run",
          "created_at": 1699063290,
          "assistant_id": "asst_abc123",
          "thread_id": "thread_abc123",
          "status": "completed",
          "started_at": 1699063290,
          "expires_at": null,
          "cancelled_at": null,
          "failed_at": null,
          "completed_at": 1699063291,
          "last_error": null,
          "model": "gpt-4-turbo",
          "instructions": null,
          "incomplete_details": null,
          "tools": [
            {
              "type": "code_interpreter"
            }
          ],
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ],
          "metadata": {},
          "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 456,
            "total_tokens": 579
          },
          "temperature": 1.0,
          "top_p": 1.0,
          "max_prompt_tokens": 1000,
          "max_completion_tokens": 1000,
          "truncation_strategy": {
            "type": "auto",
            "last_messages": null
          },
          "response_format": "auto",
          "tool_choice": "auto"
        }
      ],
      "first_id": "run_abc123",
      "last_id": "run_abc456",
      "has_more": false
    }

[

List run steps (v1)

Legacy


-----------------------------

](/docs/api-reference/runs-v1/listRunSteps)

get https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/steps

Returns a list of run steps belonging to a run.

### Path parameters

[](#runs-v1-listrunsteps-thread_id)

thread\_id

string

Required

The ID of the thread the run and run steps belong to.

[](#runs-v1-listrunsteps-run_id)

run\_id

string

Required

The ID of the run the run steps belong to.

### Query parameters

[](#runs-v1-listrunsteps-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](#runs-v1-listrunsteps-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](#runs-v1-listrunsteps-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

[](#runs-v1-listrunsteps-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

### Returns

A list of [run step](/docs/api-reference/runs-v1/step-object) objects.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/steps \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    {
      "object": "list",
      "data": [
        {
          "id": "step_abc123",
          "object": "thread.run.step",
          "created_at": 1699063291,
          "run_id": "run_abc123",
          "assistant_id": "asst_abc123",
          "thread_id": "thread_abc123",
          "type": "message_creation",
          "status": "completed",
          "cancelled_at": null,
          "completed_at": 1699063291,
          "expired_at": null,
          "failed_at": null,
          "last_error": null,
          "step_details": {
            "type": "message_creation",
            "message_creation": {
              "message_id": "msg_abc123"
            }
          },
          "usage": {
            "prompt_tokens": 123,
            "completion_tokens": 456,
            "total_tokens": 579
          }
        }
      ],
      "first_id": "step_abc123",
      "last_id": "step_abc456",
      "has_more": false
    }

[

Retrieve run (v1)

Legacy


---------------------------

](/docs/api-reference/runs-v1/getRun)

get https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}

Retrieves a run.

### Path parameters

[](#runs-v1-getrun-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads-v1) that was run.

[](#runs-v1-getrun-run_id)

run\_id

string

Required

The ID of the run to retrieve.

### Returns

The [run](/docs/api-reference/runs-v1/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    }

[

Retrieve run step (v1)

Legacy


--------------------------------

](/docs/api-reference/runs-v1/getRunStep)

get https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

Retrieves a run step.

### Path parameters

[](#runs-v1-getrunstep-thread_id)

thread\_id

string

Required

The ID of the thread to which the run and run step belongs.

[](#runs-v1-getrunstep-run_id)

run\_id

string

Required

The ID of the run to which the run step belongs.

[](#runs-v1-getrunstep-step_id)

step\_id

string

Required

The ID of the run step to retrieve.

### Returns

The [run step](/docs/api-reference/runs-v1/step-object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/steps/step_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1"

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "created_at": 1699063291,
      "run_id": "run_abc123",
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "type": "message_creation",
      "status": "completed",
      "cancelled_at": null,
      "completed_at": 1699063291,
      "expired_at": null,
      "failed_at": null,
      "last_error": null,
      "step_details": {
        "type": "message_creation",
        "message_creation": {
          "message_id": "msg_abc123"
        }
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      }
    }

[

Modify run (v1)

Legacy


-------------------------

](/docs/api-reference/runs-v1/modifyRun)

post https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}

Modifies a run.

### Path parameters

[](#runs-v1-modifyrun-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads-v1) that was run.

[](#runs-v1-modifyrun-run_id)

run\_id

string

Required

The ID of the run to modify.

### Request body

[](#runs-v1-modifyrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [run](/docs/api-reference/runs-v1/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123 \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
        "metadata": {
          "user_id": "user_abc123"
        }
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {
        "user_id": "user_abc123"
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    }

[

Submit tool outputs to run (v1)

Legacy


-----------------------------------------

](/docs/api-reference/runs-v1/submitToolOutputs)

post https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.

### Path parameters

[](#runs-v1-submittooloutputs-thread_id)

thread\_id

string

Required

The ID of the [thread](/docs/api-reference/threads-v1) to which this run belongs.

[](#runs-v1-submittooloutputs-run_id)

run\_id

string

Required

The ID of the run that requires the tool output submission.

### Request body

[](#runs-v1-submittooloutputs-tool_outputs)

tool\_outputs

array

Required

A list of tools for which the outputs are being submitted.

Show properties

[](#runs-v1-submittooloutputs-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

### Returns

The modified [run](/docs/api-reference/runs-v1/object) object matching the specified ID.

Default‍Streaming‍

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    curl https://api.openai.com/v1/threads/thread_123/runs/run_123/submit_tool_outputs \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -H "OpenAI-Beta: assistants=v1" \
      -d '{
        "tool_outputs": [
          {
            "tool_call_id": "call_001",
            "output": "70 degrees and sunny."
          }
        ]
      }'

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    {
      "id": "run_123",
      "object": "thread.run",
      "created_at": 1699075592,
      "assistant_id": "asst_123",
      "thread_id": "thread_123",
      "status": "queued",
      "started_at": 1699075592,
      "expires_at": 1699076192,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": null,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"]
                }
              },
              "required": ["location"]
            }
          }
        }
      ],
      "file_ids": [],
      "metadata": {},
      "usage": null,
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    }

[

Cancel a run (v1)

Legacy


---------------------------

](/docs/api-reference/runs-v1/cancelRun)

post https://api.openai.com/v1/threads/{thread\_id}/runs/{run\_id}/cancel

Cancels a run that is `in_progress`.

### Path parameters

[](#runs-v1-cancelrun-thread_id)

thread\_id

string

Required

The ID of the thread to which this run belongs.

[](#runs-v1-cancelrun-run_id)

run\_id

string

Required

The ID of the run to cancel.

### Returns

The modified [run](/docs/api-reference/runs-v1/object) object matching the specified ID.

Example request

curl

Select librarycurlpythonnode.js

    1
    2
    3
    4
    curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/cancel \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "OpenAI-Beta: assistants=v1" \
      -X POST

Response

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699076126,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "cancelling",
      "started_at": 1699076126,
      "expires_at": 1699076726,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": null,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": "You summarize books.",
      "tools": [
        {
          "type": "retrieval"
        }
      ],
      "file_ids": [],
      "metadata": {},
      "usage": null,
      "temperature": 1.0,
      "top_p": 1.0,
    }

[

The run object (v1)

Legacy


-----------------------------

](/docs/api-reference/runs-v1/object)

Represents an execution run on a [thread](/docs/api-reference/threads-v1).

[](#runs-v1/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](#runs-v1/object-object)

object

string

The object type, which is always `thread.run`.

[](#runs-v1/object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the run was created.

[](#runs-v1/object-thread_id)

thread\_id

string

The ID of the [thread](/docs/api-reference/threads-v1) that was executed on as a part of this run.

[](#runs-v1/object-assistant_id)

assistant\_id

string

The ID of the [assistant](/docs/api-reference/assistants-v1) used for execution of this run.

[](#runs-v1/object-status)

status

string

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`.

[](#runs-v1/object-required_action)

required\_action

object or null

Details on the action required to continue the run. Will be `null` if no action is required.

Show properties

[](#runs-v1/object-last_error)

last\_error

object or null

The last error associated with this run. Will be `null` if there are no errors.

Show properties

[](#runs-v1/object-expires_at)

expires\_at

integer or null

The Unix timestamp (in seconds) for when the run will expire.

[](#runs-v1/object-started_at)

started\_at

integer or null

The Unix timestamp (in seconds) for when the run was started.

[](#runs-v1/object-cancelled_at)

cancelled\_at

integer or null

The Unix timestamp (in seconds) for when the run was cancelled.

[](#runs-v1/object-failed_at)

failed\_at

integer or null

The Unix timestamp (in seconds) for when the run failed.

[](#runs-v1/object-completed_at)

completed\_at

integer or null

The Unix timestamp (in seconds) for when the run was completed.

[](#runs-v1/object-incomplete_details)

incomplete\_details

object or null

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

Show properties

[](#runs-v1/object-model)

model

string

The model that the [assistant](/docs/api-reference/assistants-v1) used for this run.

[](#runs-v1/object-instructions)

instructions

string

The instructions that the [assistant](/docs/api-reference/assistants-v1) used for this run.

[](#runs-v1/object-tools)

tools

array

The list of tools that the [assistant](/docs/api-reference/assistants-v1) used for this run.

Show possible types

[](#runs-v1/object-file_ids)

file\_ids

array

The list of [File](/docs/api-reference/files) IDs the [assistant](/docs/api-reference/assistants-v1) used for this run.

[](#runs-v1/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs-v1/object-usage)

usage

[](#runs-v1/object-temperature)

temperature

number or null

The sampling temperature used for this run. If not set, defaults to 1.

[](#runs-v1/object-top_p)

top\_p

number or null

The nucleus sampling value used for this run. If not set, defaults to 1.

[](#runs-v1/object-max_prompt_tokens)

max\_prompt\_tokens

integer or null

The maximum number of prompt tokens specified to have been used over the course of the run.

[](#runs-v1/object-max_completion_tokens)

max\_completion\_tokens

integer or null

The maximum number of completion tokens specified to have been used over the course of the run.

[](#runs-v1/object-truncation_strategy)

truncation\_strategy

object

Show properties

[](#runs-v1/object-tool_choice)

tool\_choice

string or object

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling a tool. Specifying a particular tool like `{"type": "TOOL_TYPE"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Show possible types

[](#runs-v1/object-response_format)

response\_format

string or object

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show possible types

The run object (v1)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1698107661,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699073476,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699073498,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "tools": [{"type": "retrieval"}, {"type": "code_interpreter"}],
      "file_ids": [],
      "metadata": {},
      "incomplete_details": null,
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    }

[

The run step object (v1)

Legacy


----------------------------------

](/docs/api-reference/runs-v1/step-object)

Represents a step in execution of a run.

[](#runs-v1/step-object-id)

id

string

The identifier of the run step, which can be referenced in API endpoints.

[](#runs-v1/step-object-object)

object

string

The object type, which is always `thread.run.step`.

[](#runs-v1/step-object-created_at)

created\_at

integer

The Unix timestamp (in seconds) for when the run step was created.

[](#runs-v1/step-object-assistant_id)

assistant\_id

string

The ID of the [assistant](/docs/api-reference/assistants-v1) associated with the run step.

[](#runs-v1/step-object-thread_id)

thread\_id

string

The ID of the [thread](/docs/api-reference/threads-v1) that was run.

[](#runs-v1/step-object-run_id)

run\_id

string

The ID of the [run](/docs/api-reference/runs-v1) that this run step is a part of.

[](#runs-v1/step-object-type)

type

string

The type of run step, which can be either `message_creation` or `tool_calls`.

[](#runs-v1/step-object-status)

status

string

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

[](#runs-v1/step-object-step_details)

step\_details

object

The details of the run step.

Show possible types

[](#runs-v1/step-object-last_error)

last\_error

object or null

The last error associated with this run step. Will be `null` if there are no errors.

Show properties

[](#runs-v1/step-object-expired_at)

expired\_at

integer or null

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

[](#runs-v1/step-object-cancelled_at)

cancelled\_at

integer or null

The Unix timestamp (in seconds) for when the run step was cancelled.

[](#runs-v1/step-object-failed_at)

failed\_at

integer or null

The Unix timestamp (in seconds) for when the run step failed.

[](#runs-v1/step-object-completed_at)

completed\_at

integer or null

The Unix timestamp (in seconds) for when the run step completed.

[](#runs-v1/step-object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](#runs-v1/step-object-usage)

usage

The run step object (v1)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "created_at": 1699063291,
      "run_id": "run_abc123",
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "type": "message_creation",
      "status": "completed",
      "cancelled_at": null,
      "completed_at": 1699063291,
      "expired_at": null,
      "failed_at": null,
      "last_error": null,
      "step_details": {
        "type": "message_creation",
        "message_creation": {
          "message_id": "msg_abc123"
        }
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      }
    }

[

Streaming (v1)

Legacy


------------------------

](/docs/api-reference/assistants-streaming-v1)

Stream the result of executing a Run or resuming a Run after submitting tool outputs.

You can stream events from the [Create Thread and Run](/docs/api-reference/runs-v1/createThreadAndRun), [Create Run](/docs/api-reference/runs-v1/createRun), and [Submit Tool Outputs](/docs/api-reference/runs-v1/submitToolOutputs) endpoints by passing `"stream": true`. The response will be a [Server-Sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) stream.

Our Node and Python SDKs provide helpful utilities to make streaming easy. Reference the [Assistants API quickstart](/docs/assistants/overview) to learn more.

[

The message delta object (v1)

Legacy


---------------------------------------

](/docs/api-reference/assistants-streaming-v1/message-delta-object)

Represents a message delta i.e. any changed fields on a message during streaming.

[](#assistants-streaming-v1/message-delta-object-id)

id

string

The identifier of the message, which can be referenced in API endpoints.

[](#assistants-streaming-v1/message-delta-object-object)

object

string

The object type, which is always `thread.message.delta`.

[](#assistants-streaming-v1/message-delta-object-delta)

delta

object

The delta containing the fields that have changed on the Message.

Show properties

The message delta object (v1)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    {
      "id": "msg_123",
      "object": "thread.message.delta",
      "delta": {
        "content": [
          {
            "index": 0,
            "type": "text",
            "text": { "value": "Hello", "annotations": [] }
          }
        ]
      }
    }

[

The run step delta object (v1)

Legacy


----------------------------------------

](/docs/api-reference/assistants-streaming-v1/run-step-delta-object)

Represents a run step delta i.e. any changed fields on a run step during streaming.

[](#assistants-streaming-v1/run-step-delta-object-id)

id

string

The identifier of the run step, which can be referenced in API endpoints.

[](#assistants-streaming-v1/run-step-delta-object-object)

object

string

The object type, which is always `thread.run.step.delta`.

[](#assistants-streaming-v1/run-step-delta-object-delta)

delta

object

The delta containing the fields that have changed on the run step.

Show properties

The run step delta object (v1)

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    {
      "id": "step_123",
      "object": "thread.run.step.delta",
      "delta": {
        "step_details": {
          "type": "tool_calls",
          "tool_calls": [
            {
              "index": 0,
              "id": "call_123",
              "type": "code_interpreter",
              "code_interpreter": { "input": "", "outputs": [] }
            }
          ]
        }
      }
    }

[

Assistant stream events (v1)

Legacy


--------------------------------------

](/docs/api-reference/assistants-streaming-v1/events)

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

    event: thread.created
    data: {"id": "thread_123", "object": "thread", ...}

We emit events whenever a new object is created, transitions to a new state, or is being streamed in parts (deltas). For example, we emit `thread.run.created` when a new run is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses to create a message during a run, we emit a `thread.message.created event`, a `thread.message.in_progress` event, many `thread.message.delta` events, and finally a `thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully in your code. See the [Assistants API quickstart](/docs/assistants/overview) to learn how to integrate the Assistants API with streaming.

[](#assistants-streaming-v1/events-thread-created)

thread.created

`data` is a [thread](/docs/api-reference/threads-v1/object)

Occurs when a new [thread](/docs/api-reference/threads-v1/object) is created.

[](#assistants-streaming-v1/events-thread-run-created)

thread.run.created

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a new [run](/docs/api-reference/runs-v1/object) is created.

[](#assistants-streaming-v1/events-thread-run-queued)

thread.run.queued

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) moves to a `queued` status.

[](#assistants-streaming-v1/events-thread-run-in_progress)

thread.run.in\_progress

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) moves to an `in_progress` status.

[](#assistants-streaming-v1/events-thread-run-requires_action)

thread.run.requires\_action

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) moves to a `requires_action` status.

[](#assistants-streaming-v1/events-thread-run-completed)

thread.run.completed

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) is completed.

[](#assistants-streaming-v1/events-thread-run-failed)

thread.run.failed

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) fails.

[](#assistants-streaming-v1/events-thread-run-cancelling)

thread.run.cancelling

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) moves to a `cancelling` status.

[](#assistants-streaming-v1/events-thread-run-cancelled)

thread.run.cancelled

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) is cancelled.

[](#assistants-streaming-v1/events-thread-run-expired)

thread.run.expired

`data` is a [run](/docs/api-reference/runs-v1/object)

Occurs when a [run](/docs/api-reference/runs-v1/object) expires.

[](#assistants-streaming-v1/events-thread-run-step-created)

thread.run.step.created

`data` is a [run step](/docs/api-reference/runs-v1/step-object)

Occurs when a [run step](/docs/api-reference/runs-v1/step-object) is created.

[](#assistants-streaming-v1/events-thread-run-step-in_progress)

thread.run.step.in\_progress

`data` is a [run step](/docs/api-reference/runs-v1/step-object)

Occurs when a [run step](/docs/api-reference/runs-v1/step-object) moves to an `in_progress` state.

[](#assistants-streaming-v1/events-thread-run-step-delta)

thread.run.step.delta

`data` is a [run step delta](/docs/api-reference/assistants-streaming-v1/run-step-delta-object)

Occurs when parts of a [run step](/docs/api-reference/runs-v1/step-object) are being streamed.

[](#assistants-streaming-v1/events-thread-run-step-completed)

thread.run.step.completed

`data` is a [run step](/docs/api-reference/runs-v1/step-object)

Occurs when a [run step](/docs/api-reference/runs-v1/step-object) is completed.

[](#assistants-streaming-v1/events-thread-run-step-failed)

thread.run.step.failed

`data` is a [run step](/docs/api-reference/runs-v1/step-object)

Occurs when a [run step](/docs/api-reference/runs-v1/step-object) fails.

[](#assistants-streaming-v1/events-thread-run-step-cancelled)

thread.run.step.cancelled

`data` is a [run step](/docs/api-reference/runs-v1/step-object)

Occurs when a [run step](/docs/api-reference/runs-v1/step-object) is cancelled.

[](#assistants-streaming-v1/events-thread-run-step-expired)

thread.run.step.expired

`data` is a [run step](/docs/api-reference/runs-v1/step-object)

Occurs when a [run step](/docs/api-reference/runs-v1/step-object) expires.

[](#assistants-streaming-v1/events-thread-message-created)

thread.message.created

`data` is a [message](/docs/api-reference/messages-v1/object)

Occurs when a [message](/docs/api-reference/messages-v1/object) is created.

[](#assistants-streaming-v1/events-thread-message-in_progress)

thread.message.in\_progress

`data` is a [message](/docs/api-reference/messages-v1/object)

Occurs when a [message](/docs/api-reference/messages-v1/object) moves to an `in_progress` state.

[](#assistants-streaming-v1/events-thread-message-delta)

thread.message.delta

`data` is a [message delta](/docs/api-reference/assistants-streaming-v1/message-delta-object)

Occurs when parts of a [Message](/docs/api-reference/messages-v1/object) are being streamed.

[](#assistants-streaming-v1/events-thread-message-completed)

thread.message.completed

`data` is a [message](/docs/api-reference/messages-v1/object)

Occurs when a [message](/docs/api-reference/messages-v1/object) is completed.

[](#assistants-streaming-v1/events-thread-message-incomplete)

thread.message.incomplete

`data` is a [message](/docs/api-reference/messages-v1/object)

Occurs when a [message](/docs/api-reference/messages-v1/object) ends before it is completed.

[](#assistants-streaming-v1/events-error)

error

`data` is an [error](/docs/guides/error-codes/api-errors)

Occurs when an [error](/docs/guides/error-codes/api-errors) occurs. This can happen due to an internal server error or a timeout.

[](#assistants-streaming-v1/events-done)

done

`data` is `[DONE]`

Occurs when a stream ends.
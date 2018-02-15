CREATE TABLE individual (
    id integer NOT NULL PRIMARY KEY,
    name character varying(600) NOT NULL
);

CREATE SEQUENCE individual_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


CREATE TABLE variant (
    id           int PRIMARY KEY,
    chr            varchar(20),
    pos            int,
    snpid            varchar(50),
    ref            varchar(80),
    alt            text,
    qual            real,
    filter            text,
    info            text,
    depth           int,
    format            text,
    genotype            text
);

CREATE SEQUENCE variants_variant_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE INDEX variant_id_1073f3b5 ON variant USING btree (id);

ALTER TABLE variant OWNER TO raony;
GRANT ALL PRIVILEGES ON DATABASE bench TO raony;
ALTER TABLE individual OWNER TO raony;